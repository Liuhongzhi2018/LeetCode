#   Minimum Window Substring

## 问题描述

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。

## 代码实现

1.
```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i = 0
        res = (0, float('inf'))
        for j, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:
                while True:
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:
                    res = (i, j)
                need[s[i]] += 1
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1]+1]

```


## 思路总结

首先由于数组长度为n，所以答案一定在[1,n+1]之中出现，所以第一轮把无关项全部剔除改为0；  
需要给数组长度为n的数组加上2个尾部元素(2^31)，因为该元素的下标为n，而我们需要记录一直到n+1的，所以添加两个元素； 
第二轮遍历，因为现在数字的范围是在[0,n+1]中，可以想一个办法在原数组中标记出现过的n；  
标记方法是将出现过的k的下标位置的元素变为负数，以此标记出现过的k； 
第三轮遍历下标，从1开始到n+1结束，当有元素是大于等于0时，返回当前下标。

defaultdict还可以被用来计数，将default_factory设为int即可。 
collections.defaultdict([default_factory[, …]])
参考  https://blog.csdn.net/yangsong95/article/details/82319675