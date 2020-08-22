#  Integer Break

## 问题描述

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。


## 代码实现

1.动态规划
```python
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1) 
        for i in range(2, n + 1): 
            for j in range(i): 
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j]) 
        return dp[n] 
```

2.优化动态规划
```python
class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4: 
            return n - 1 
        
        dp = [0] * (n + 1) 
        dp[2] = 1 
        for i in range(3, n + 1): 
            dp[i] = max(2 * (i - 2), 2 * dp[i - 2], 3 * (i - 3), 3 * dp[i - 3]) 
            
        return dp[n]
```


## 思路总结

对于的正整数 n，当 n≥2 时，可以拆分成至少两个正整数的和。令 k 是拆分出的第一个正整数，则剩下的部分是 n−k 可以不继续拆分，或者继续拆分成至少两个正整数的和。由于每个正整数对应的最大乘积取决于比它小的正整数对应的最大乘积，因此可以使用动态规划求解。

创建数组 dp\text{dp}dp，其中 dp[i] 表示将正整数 i 拆分成至少两个正整数的和之后，这些正整数的最大乘积。特别地，0 不是正整数，1 是最小的正整数，0 和 1 都不能拆分，因此 dp[0]=dp[1]=0。
