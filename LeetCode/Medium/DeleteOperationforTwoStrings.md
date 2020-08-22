#  Delete Operation for Two Strings

## 问题描述

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string. 

给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。


## 代码实现

1.动态规划
```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1=len(word1) 
        n2=len(word2) 
        if not n1:
            return n2 
        if not n2:
            return n1 
            
        dp=[[0 for i in range(n2+1)]
        for i in range(n1+1)] 
        for i in range(1,n1+1): 
            for j in range(1,n2+1): 
                if word1[i-1]==word2[j-1]: 
                    dp[i][j]=dp[i-1][j-1]+1 
                else: 
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                    ##dp[n1][n2]中保存的就是二者的最长子序列 
        return n1+n2-2*dp[n1][n2]
        ##二者把最长子序列以外的字符删除就好了 
```


## 思路总结

