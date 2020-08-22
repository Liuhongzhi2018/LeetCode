#  Coin Change 2

## 问题描述

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

## 代码实现

1.
```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1) 
        dp[0] = 1 
        for coin in coins: 
            for x in range(coin, amount + 1): 
                dp[x] += dp[x - coin] 
        return dp[amount]
```


## 思路总结

动态规划模板：
这是经典的动态编程问题。这是一个可以使用的模板：

    定义答案显而易见的基本情况。
    制定根据简单的情况计算复杂情况的策略。
    将此策略链接到基本情况。
