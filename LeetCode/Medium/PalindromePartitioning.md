#  Palindrome Partitioning

## 问题描述

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。


## 代码实现

1.回溯法
```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        if len(s) == 0:
            return res

        def backtrack(start=0, ss=[]):
            if start >= len(s):
                res.append(ss)
                return 
            
            for cur in range(start+1, len(s)+1):
                sps = s[start:cur]
                if sps == s[start:cur][::-1]:
                    backtrack(cur, ss+[sps])

        backtrack()
        return res
```


## 思路总结

回溯法， 首先定义一个列表res保存最终结果，如果给定字符串为空则直接返回。  
在回溯时进行判断，如果当前子串为回文串则继续递归。