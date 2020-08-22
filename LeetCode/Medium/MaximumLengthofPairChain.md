#  Maximum Length of Pair Chain

## 问题描述

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。

现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。

给定一个对数集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。

## 代码实现

1.动态规划
```python
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort() 
        dp = [1] * len(pairs) 
        for j in range(len(pairs)): 
            for i in range(j): 
                if pairs[i][1] < pairs[j][0]: 
                    dp[j] = max(dp[j], dp[i] + 1) 
                    
        return max(dp) 
```

2.贪心算法
```python
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, ans = float('-inf'), 0 
        for x, y in sorted(pairs, key = operator.itemgetter(1)): 
            if cur < x: 
                cur = y 
                ans += 1 
        return ans
```


## 思路总结

