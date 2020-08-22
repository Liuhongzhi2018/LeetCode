#  Decode Ways

## 问题描述

A message containing letters from A-Z is being encoded to numbers using the following mapping:

Given a non-empty string containing only digits, determine the total number of ways to decode it.

一条包含字母 A-Z 的消息通过以下方式进行了编码：

给定一个只包含数字的非空字符串，请计算解码方法的总数。


## 代码实现

1.
```python
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [1,0]
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(1,n):
            dp.append(0)
            if s[i]!='0':
                dp[i+1] += dp[i]
            if s[i-1:i+1]>='10' and s[i-1:i+1]<='26':
                dp[i+1] += dp[i-1]

        return dp[-1]
```

2.
```python
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0: 
            return 0
        dp = [1,0]
        dp[1] = 1 if s[0]!='0' else 0 
        for i in range(1,n):
            dp.append(0)
            if s[i]!='0': 
                dp[-1] += dp[-2] 
            if s[i-1:i+1]>='10' and s[i-1:i+1]<='26': 
                dp[-1] += dp[-3] 
            dp.pop(0) 
        return dp[-1]
```


## 思路总结

解决这道题一个比较的解高效方法便是动态规划。  
首先，大家还记得爬楼梯问题么，一共有n个台阶，一次只能向上走一阶或者两阶，问一共有多少种走法？  
这是个很经典的动态规划问题，用dp[n]表示爬完n个台阶的方法总数，那么最后一步可能是走了一阶，也可能是走了两阶，而走了一阶的方法总数等于爬完n-1个台阶的方法综述，最后一步走两阶的方法综述等于爬完n-2阶方法总数，因此不考虑边界的话可以有公式：  
dp[n] = dp[n-1]+dp[n-2]