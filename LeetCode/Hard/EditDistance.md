#  N-Queens 

## 问题分析

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

    插入一个字符
    删除一个字符
    替换一个字符


## 代码实现

1.动态规划
```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1) 
        m = len(word2) 
        
        # 有一个字符串为空串 
        if n * m == 0: 
            return n + m 
        
        # DP 数组 
        D = [ [0] * (m + 1) for _ in range(n + 1)] 
        
        # 边界状态初始化 
        for i in range(n + 1): 
            D[i][0] = i 
        for j in range(m + 1): 
            D[0][j] = j 
            
        # 计算所有 DP 值 
        for i in range(1, n + 1): 
            for j in range(1, m + 1): 
                left = D[i - 1][j] + 1 
                down = D[i][j - 1] + 1 
                left_down = D[i - 1][j - 1] 
                if word1[i - 1] != word2[j - 1]: 
                    left_down += 1 
                D[i][j] = min(left, down, left_down) 
        return D[n][m]
```


## 思路总结

思路和算法

我们可以对任意一个单词进行三种操作：

    插入一个字符；

    删除一个字符；

    替换一个字符。

题目给定了两个单词，设为 A 和 B，这样我们就能够六种操作方法。

但我们可以发现，如果我们有单词 A 和单词 B：

    对单词 A 删除一个字符和对单词 B 插入一个字符是等价的。例如当单词 A 为 doge，单词 B 为 dog 时，我们既可以删除单词 A 的最后一个字符 e，得到相同的 dog，也可以在单词 B 末尾添加一个字符 e，得到相同的 doge；

    同理，对单词 B 删除一个字符和对单词 A 插入一个字符也是等价的；

    对单词 A 替换一个字符和对单词 B 替换一个字符是等价的。例如当单词 A 为 bat，单词 B 为 cat 时，我们修改单词 A 的第一个字母 b -> c，和修改单词 B 的第一个字母 c -> b 是等价的。

这样以来，本质不同的操作实际上只有三种：

    在单词 A 中插入一个字符；

    在单词 B 中插入一个字符；

    修改单词 A 的一个字符。

这样以来，我们就可以把原问题转化为规模较小的子问题。我们用 A = horse，B = ros 作为例子，来看一看是如何把这个问题转化为规模较小的若干子问题的。