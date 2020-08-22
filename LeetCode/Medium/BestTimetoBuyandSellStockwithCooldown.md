#  Best Time to Buy and Sell Stock with Cooldown

## 问题描述

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
    
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

    你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。


## 代码实现

1.
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: 
            return 0 
        n = len(prices) 
        # f[i][0]: 手上持有股票的最大收益 
        # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益 
        # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益 
        f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)] 
        for i in range(1, n): 
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i]) 
            f[i][1] = f[i - 1][0] + prices[i] 
            f[i][2] = max(f[i - 1][1], f[i - 1][2]) 
            
        return max(f[n - 1][1], f[n - 1][2])
```


## 思路总结

