#  Combination Sum IV

## 问题描述

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。


## 代码实现

1.
```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0 
        dp = [0] * (target+1) 
        dp[0] = 1 
        for i in range(1,target+1): 
            for num in nums: 
                if i >= num: 
                    dp[i] += dp[i-num] 
        return dp[target]
```


## 思路总结
