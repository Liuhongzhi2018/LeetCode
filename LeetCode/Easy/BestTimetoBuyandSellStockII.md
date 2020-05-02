#  Best Time to Buy and Sell Stock II

## 问题分析
Say you have an array for which the i<sup>th</sup> element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

## 代码实现
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

## 总结体会

本题尽可能完成多次交易求最大利润，与上一题求数组最大顺序差值不同，本题采用的方法是求邻域内的最小值和最大值，以求得的最大利润和的方法。

算法设计上采用while循环语句，首先求得邻域内最小值，保存在min变量中，其次求得邻域内最大值，利润profit为该邻域最大值与最小值差值，依次计算，求得最大利润值返回。同样，为提高计算效率，若数组元素小于2，则返回0值。











