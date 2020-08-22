#  Ones and Zeroes

## 问题描述

Given an array, strs, with strings consisting of only 0s and 1s. Also two integers m and n.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

在计算机界中，我们总是追求用有限的资源获取最大的收益。

现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。

你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。

注意:

    给定 0 和 1 的数量都不会超过 100。
    给定字符串数组的长度不会超过 600。

## 代码实现

1.
```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)] 
        for s in strs: 
            c0 = s.count('0') 
            c1 = len(s) - c0 
            for i in range(m, c0 - 1, -1): 
                for j in range(n, c1 - 1, -1): 
                    dp[i][j] = max(dp[i][j], dp[i - c0][j - c1] + 1)
        return dp[m][n]
```


## 思路总结

