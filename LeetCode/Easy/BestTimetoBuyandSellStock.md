#  Best Time to Buy and Sell Stock

## 问题分析
Say you have an array for which the i<sup>th</sup> element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

## 代码实现
``` C
int maxProfit(int* prices, int pricesSize) {
    int i, j;
    int max=0,temp;
    int n = pricesSize;
    if (n < 2) {
        return 0;
    }
    for (i = 0; i < n; i++) {
        for (j = i; j < n; j++) {
            if (prices[j] - prices[i] < 0)
                continue;
            else temp = prices[j] - prices[i];
            if (temp > max) max = temp;
        }
    }
    return max;
}
```

## 总结体会

本题要求最大利润，可以转换为按数组元素排列顺序，求后项与前项最大差值的思想。

在求后项与前项差值时，用temp变量保存差值，如果比当前max值大则赋值给max，否则max值不变。为提高计算效率，当数组元素小于或者等于1时，最大差值均为0，因为只有一个元素和自己作减法显然为0。

本题较为简单，第一次OJ可以Accepted。同时在编辑本文问题分析部分时，学习了markdown上标的写法，即sup和/sup间加上标内容th，显示为i的上标th。











