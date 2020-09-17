#  2 Keys Keyboard

## 问题描述

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

    Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
    Paste: You can paste the characters which are copied last time.

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作：

    Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。
    Paste (粘贴) : 你可以粘贴你上一次复制的字符。

给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。


## 代码实现

1.动态规划
```python
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1: 
            return 0 
        dp = [[n]*n for _ in range(n)] 
        #dp[i][j] 记事本上有i+1个A，粘贴板上有j+1个A 
        dp[0][0] = 1 
        for i in range(1,n): 
            for j in range(i): 
                dp[i][j] = dp[i-j-1][j] + 1 
            dp[i][i] = min(dp[i]) + 1 
        return dp[-1][-1] -1
```


## 思路总结

