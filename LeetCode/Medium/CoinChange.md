#  Coin Change

## 问题描述

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。


## 代码实现

1.动态规划-自上而下
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(amount)
        def dp(rem):
            if rem < 0: 
                return -1 
            if rem == 0: 
                return 0 
            mini = int(1e9)
            for coin in self.coins: 
                res = dp(rem - coin) 
                if res >= 0 and res < mini: 
                    mini = res + 1 
            return mini if mini < int(1e9) else -1 
        
        self.coins = coins 
        if amount < 1: 
            return 0 
        return dp(amount)
```

2. 动态规划：自下而上
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1) 
        dp[0] = 0 
        
        for coin in coins: 
            for x in range(coin, amount + 1): 
                dp[x] = min(dp[x], dp[x - coin] + 1) 
        
        return dp[amount] if dp[amount] != float('inf') else -1 
```


## 思路总结

我们注意到这个问题有一个最优的子结构性质，这是解决动态规划问题的关键。最优解可以从其子问题的最优解构造出来。如何将问题分解成子问题？假设我们知道 F(S) ，即组成金额 S 最少的硬币数，最后一枚硬币的面值是 C。