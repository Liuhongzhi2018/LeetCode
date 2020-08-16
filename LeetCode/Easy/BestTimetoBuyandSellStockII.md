#  Best Time to Buy and Sell Stock II

## 问题分析

Say you have an array for which the i<sup>th</sup> element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

## 代码实现

1.
``` C
int maxProfit(int* prices, int pricesSize) {
    int i = 0;
    int n = pricesSize;
    if (n < 2) {
        return 0;
    }
    int profit = 0;
    while (i < n) {
        while (i < n - 1 && prices[i + 1] <= prices[i]) i++;
        int min = prices[i++];
        while (i < n - 1 && prices[i + 1] >= prices[i]) i++;
        if (i < n)  profit += prices[i++] - min;
           else profit += 0;
    }
    return profit;
}
```

2.
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        pf = 0
        for i in range(1,n):
            tmp = prices[i] - prices[i-1]
            if tmp > 0:
                pf += tmp
        return pf
```

## 总结体会

本题尽可能完成多次交易求最大利润，与上一题求数组最大顺序差值不同，本题采用的方法是求邻域内的最小值和最大值，以求得的最大利润和的方法。

算法设计上采用while循环语句，首先求得邻域内最小值，保存在min变量中，其次求得邻域内最大值，利润profit为该邻域最大值与最小值差值，依次计算，求得最大利润值返回。同样，为提高计算效率，若数组元素小于2，则返回0值。

股票买卖策略：  
单独交易日： 设今天价格 p1p_1p1​、明天价格 p2p_2p2​，则今天买入、明天卖出可赚取金额 p2−p1p_2 - p_1p2​−p1​ （负值代表亏损）。  
连续上涨交易日： 设此上涨交易日股票价格分别为 p1,p2,...,pnp_1, p_2, ... , p_np1​,p2​,...,pn​，则第一天买最后一天卖收益最大，即 pn−p1p_n - p_1pn​−p1​；等价于每天都买卖，即 pn−p1=(p2−p1)+(p3−p2)+...+(pn−pn−1)p_n - p_1=(p_2 - p_1)+(p_3 - p_2)+...+(p_n - p_{n-1})pn​−p1​=(p2​−p1​)+(p3​−p2​)+...+(pn​−pn−1​)。  
连续下降交易日： 则不买卖收益最大，即不会亏钱。

算法流程：
遍历整个股票交易日价格列表 price，策略是所有上涨交易日都买卖（赚到所有利润），所有下降交易日都不买卖（永不亏钱）。  
设 tmp 为第 i-1 日买入与第 i 日卖出赚取的利润，即 tmp = prices[i] - prices[i - 1] ；  
当该天利润为正 tmp > 0，则将利润加入总利润 profit；当利润为 000 或为负，则直接跳过；  
遍历完成后，返回总利润 profit。

复杂度分析：
时间复杂度 O(N)O(N)O(N) ： 只需遍历一次price；  
空间复杂度 O(1)O(1)O(1) ： 变量使用常数额外空间。









