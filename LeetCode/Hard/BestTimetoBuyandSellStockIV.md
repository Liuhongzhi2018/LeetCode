#   Best Time to Buy and Sell Stock IV

## 问题描述

Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


## 代码实现

1.动态规划
```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices) 
        if n <= 1: return 0 
        
        if k >= n//2: 
            # 退化为不限制交易次数 
            profit = 0 
            for i in range(1, n): 
                if prices[i] > prices[i - 1]: 
                    profit += prices[i] - prices[i - 1] 
            return profit 
        else: 
            # 限制交易次数为k 
            dp = [[[None, None] for _ in range(k+1)] for _ in range(n)] # (n, k+1, 2) 
            for i in range(n): 
                dp[i][0][0] = 0 
                dp[i][0][1] = -float('inf') 
            for j in range(1, k+1): 
                dp[0][j][0] = 0 
                dp[0][j][1] = -prices[0] 
            for i in range(1, n): 
                for j in range(1, k+1): 
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i]) 
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i]) 
        return dp[-1][-1][0]
```


## 思路总结

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/solution/gu-piao-jiao-yi-xi-lie-cong-tan-xin-dao-dong-tai-g/

股票系列一共 6 道题：

    LeetCode 121：最多进行 1 笔交易（k=1）【贪心】
    LeetCode 122：不限交易次数（k=+inf）【二维 DP】
        LeetCode 309：不限交易次数（k=+inf），但有「冷冻期」的额外条件
        LeetCode 714：不限交易次数（k=+inf），但有「手续费」的额外条件
    LeetCode 123：最多进行 2 笔交易（k=2）【三维 DP】
        LeetCode 188：最多进行 k 次交易

