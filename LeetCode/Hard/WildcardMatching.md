#  Wildcard Matching

## 问题分析

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like ? or *.


给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 ' * ' 的通配符匹配。

两个字符串完全匹配才算匹配成功。

说明:

    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。


## 代码实现

1.
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = [-1,-1]
        p_ptr, s_ptr = 0,0
        while s_ptr<len(s):
            if p_ptr<len(p) and p[p_ptr] in (s[s_ptr],'?','*'):
                if p[p_ptr]=='*':
                    cache[0],cache[1]=p_ptr,s_ptr
                else:
                    s_ptr += 1
                p_ptr += 1
            elif cache[0] != -1:
                p_ptr,s_ptr = cache[0]+1,cache[1]+1
                cache[1]+=1
            else:
                return False
        while p_ptr<len(p) and p[p_ptr]=='*':
            p_ptr += 1
        return (p_ptr == len(p))
```


## 思路总结

用两个指针分别代表p匹配字符串和s字符串的下标指针，cache用于存储' * '位置以及对应s下标的指针位置，初始值[-1,-1]；  
最开始 * 先匹配0个字符，但仍需要更新cache；
