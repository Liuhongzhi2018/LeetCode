#  Best Time to Buy and Sell Stock with Transaction Fee

## 问题描述

Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

## 代码实现

1.
```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0] 
        for i in range(1, len(prices)): 
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i]) 
        return cash
```


## 思路总结

我们维护两个变量 cash 和 hold，前者表示当我们不持有股票时的最大利润，后者表示当我们持有股票时的最大利润。

在第 i 天时，我们需要根据第 i−1 天的状态来更新 cash 和 hold 的值。对于 cash，我们可以保持不变，或者将手上的股票卖出，状态转移方程为

cash = max(cash, hold + prices[i] - fee)

对于 hold，我们可以保持不变，或者买入这一天的股票，状态转移方程为

hold = max(hold, cash - prices[i])

在计算这两个状态转移方程时，我们可以不使用临时变量来存储第 i−1 天 cash 和 hold 的值，而是可以先计算 cash 再计算 hold，原因是在同一天卖出再买入（亏了一笔手续费）一定不会比不进行任何操作好。