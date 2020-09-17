#   Best Time to Buy and Sell Stock III

## 问题描述

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


## 代码实现

1.动态规划
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: 
            return 0 
        n = len(prices) 
        
        # 定义三维数组，第i天、交易了多少次、当前的买卖状态 
        dp = [[[-1 for _ in range(2)] for _ in range(3)] for _ in range(n)] 
        
        # 初始化第一天，这里的dp[0][2][1]可以不用管，后面也不会用到 
        dp[0][0][0] = 0 
        dp[0][0][1] = -prices[0] 
        dp[0][1][0] = 0 
        dp[0][1][1] = -prices[0] 
        dp[0][2][0] = 0 
        dp[0][2][1] = -prices[0] 
        
        for i in range(1,n): 
            # dp[i][0][0]相当于初始状态，它只能从初始状态转换来 
            dp[i][0][0] = dp[i-1][0][0] 
            # 处理第一次买入、第一次卖出 
            dp[i][0][1] = max(dp[i-1][0][1],dp[i-1][0][0]-prices[i]) 
            dp[i][1][0] = max(dp[i-1][1][0],dp[i-1][0][1]+prices[i]) 
            
            # 处理第二次买入、第二次卖出 
            dp[i][1][1] = max(dp[i-1][1][1],dp[i-1][1][0]-prices[i])
            dp[i][2][0] = max(dp[i-1][2][0],dp[i-1][1][1]+prices[i]) 
            
        # 返回最大值 
        return max(dp[-1][0][0],dp[-1][0][1],dp[-1][1][0],dp[-1][1][1],dp[-1][2][0])
```


## 思路总结

状态转换公式推导  
前面我们分析过了，买入1这个状态只能从两个地方转换来，买入1本身(保持不动)，或者是初始状态转换而来。
而卖出1这个状态，也只能从两个地方转换而来，卖出1本身(保持不动)，或者从买入1转来。

那么根据上面描述，我们可以算出第一次买卖的DP公式：

第一次买入：从初始状态转换而来，或者第一次买入后保持不动
dp[i][0][1] = max(dp[i-1][0][1],dp[i-1][0][0]-prices[i])

第一次卖出：从第一次买入转换而来，或者第一次卖出后保持不动
dp[i][1][0] = max(dp[i-1][1][0],dp[i-1][0][1]+prices[i])

再来分下一下第二次的买卖过程：
同样，第二次买入只能从 第一次买入转换来，或者保持不动
第二次卖出只能从第二次买入转换来，或者保持不动

那么根据上面描述，我们可以算出第二次买卖的DP公式：

第二次买入：从第一次卖出转换而来，或者第二次买入后保持不动
dp[i][1][1] = max(dp[i-1][1][1],dp[i-1][1][0]-prices[i])

第二次卖出：从第二次买入转换而来，或者第二次卖出后保持不动
dp[i][2][0] = max(dp[i-1][2][0],dp[i-1][1][1]+prices[i])

我们把第一次买卖、第二次买卖的DP公式合到一起，就拿到了完整的推导过程。
之后我们还需要处理一下 第一天的初始化状态(具体请看代码部分)
最后求的利润最大值就保存在 dp[n-1][0][0]、dp[n-1][0][1]、dp[n-1][1][0]、dp[n-1][1][1]、dp[n-1][2][0]中，我们求出这几个值的max再返回就可以了。
