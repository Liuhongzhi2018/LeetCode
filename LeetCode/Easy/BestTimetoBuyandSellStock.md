#  Best Time to Buy and Sell Stock

## 问题分析

Say you have an array for which the i<sup>th</sup> element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

## 代码实现

1.
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

2.
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minpf = float("inf")
        maxpf = 0
        for price in prices:
            minpf = min(minpf, price)
            maxpf = max(maxpf, price-minpf)
        return maxpf
```

3.动态规划
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day = len(prices)
        if day < 2:
            return 0
        minval = prices[0]
        dp = [0] * day
        for i in range(1, day):
            minval = minval if minval < prices[i] else prices[i]
            dp[i] = dp[i-1] if prices[i]-minval<dp[i-1] else prices[i]-minval
        return dp[-1] 
```

## 总结体会

本题要求最大利润，可以转换为按数组元素排列顺序，求后项与前项最大差值的思想。

在求后项与前项差值时，用temp变量保存差值，如果比当前max值大则赋值给max，否则max值不变。为提高计算效率，当数组元素小于或者等于1时，最大差值均为0，因为只有一个元素和自己作减法显然为0。

本题较为简单，第一次OJ可以Accepted。同时在编辑本文问题分析部分时，学习了markdown上标的写法，即sup和/sup间加上标内容th，显示为i的上标th。

首先定义一个minprice=float('inf'),将minfprice定义为极大值。接着maxprofit=0，利润为0。  
之后将prices带入price迭代，minprice为minprice,price之间，因为这里是有个先后的，所以minprice得到的价格一定是当前迭代之前和当前迭代的最小值，所以不用担心是使用的后面的数值。  
接着maxprofit在maxprofit，与price-minprice之间选择，全部迭代完，输出最大值。

动态规划方法

一般分为一维、二维、多维（使用状态压缩），对应形式为 dp(i)、dp(i)(j)、二进制dp(i)(j)。

1. 动态规划做题步骤  
明确 dp(i) 应该表示什么（二维情况：dp(i)(j))；  
根据 dp(i)和 dp(i−1)的关系得出状态转移方程；  
确定初始条件，如 dp(0)。

2. 本题思路  
这里介绍一维动态规划思想。  
dp[i] 表示前i天的最大利润，因为我们始终要使利润最大化，则：  
dp[i] = max(dp[i−1],prices[i]−minprice)






