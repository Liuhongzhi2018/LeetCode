#  House Robber II

## 问题描述

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。


## 代码实现

1.动态规划
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        nums1 = nums[1:]
        nums2 = nums[0:len(nums)-1]

        def robmax(nums):
            nums_len = len(nums)
            if not nums:
                return 0
            if nums_len == 1:
                return nums[0]

            dp = [0] * nums_len
            dp[0] = nums[0]
            dp[1] = nums[1] if nums[0] < nums[1] else nums[0]  

            for i in range(2, nums_len):
                dp[i] = dp[i-1] if dp[i-2]+nums[i] < dp[i-1] else dp[i-2]+nums[i] 
            return dp[nums_len-1]

        return robmax(nums1) if robmax(nums1)>robmax(nums2) else robmax(nums2)
```


## 思路总结

动态规划方法，把题目分成两个部分：在 [0:n-1] 中找到最大值，在 [1:n] 中找到最大值。
