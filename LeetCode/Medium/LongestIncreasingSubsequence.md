#  Longest Increasing Subsequence

## 问题描述

Given an unsorted array of integers, find the length of longest increasing subsequence.

给定一个无序的整数数组，找到其中最长上升子序列的长度。


## 代码实现

1.动态规划
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: 
            return 0 
        dp = [] 
        for i in range(len(nums)): 
            dp.append(1) 
            for j in range(i): 
                if nums[i] > nums[j]: 
                    dp[i] = max(dp[i], dp[j] + 1) 
        return max(dp)
```

2.贪心 + 二分查找
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = [] 
        for n in nums: 
            if not d or n > d[-1]: 
                d.append(n) 
            else: 
                l, r = 0, len(d) - 1 
                loc = r 
                
                while l <= r: 
                    mid = (l + r) // 2 
                    if d[mid] >= n: 
                        loc = mid 
                        r = mid - 1 
                    else: 
                        l = mid + 1 
                d[loc] = n 
        
        return len(d)

```


## 思路总结

动态规划思路与算法  
定义 dp[i]为考虑前 i 个元素，以第 i 个数字结尾的最长上升子序列的长度，注意 nums[i]必须被选取。  
我们从小到大计算 dp[]数组的值，在计算 dp[i]之前，我们已经计算出 dp[0…i−1]的值，则状态转移方程为：  
dp[i]=max(dp[j])+1,其中 0≤j<i 且 num[j]<num[i]。

贪心 + 二分查找思路与算法  
考虑一个简单的贪心，如果我们要使上升子序列尽可能的长，则我们需要让序列上升得尽可能慢，因此我们希望每次在上升子序列最后加上的那个数尽可能的小。  
基于上面的贪心思路，我们维护一个数组 d[i]，表示长度为 i的最长上升子序列的末尾元素的最小值，用 len记录目前最长上升子序列的长度，起始时 len 为 1，d[1]=nums[0]。