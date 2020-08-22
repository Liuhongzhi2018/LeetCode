#  Longest Common Subsequence

## 问题描述

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

## 代码实现

1.动态规划
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1),len(text2) 
        dp = [[0]*(m+1) for _ in range(n+1)] 
        for i in range(1,n+1): 
            for j in range(1,m+1): 
                if text1[i-1]==text2[j-1]: 
                    dp[i][j]=dp[i-1][j-1]+1 
                else: 
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1]) 
        return(dp[n][m])
```


## 思路总结

最长公共子序列（lcs）是一道二维动态规划问题，难点在于有两个变量i,j在同时变化，不好理解与思考状态转移方程。
解决方法，思考时，把二维想成一维，即固定text1的i，让j去text1[:i]&text2中找最长公共子序列。
text1[i]=text2[j]时，dp[i][j]=dp[i-1][j-1]+1
text1[i]!=text2[j]时，就要比较最大值是在text1[:i]中，还是text[:i-1]中，dp[i][j]=max(dp[i-1][j],dp[i][j-1])