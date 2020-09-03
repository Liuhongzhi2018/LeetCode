#  Minimum Size Subarray Sum

## 问题描述

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。


## 代码实现

1. 双指针法
```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        lp, rp = 0, 0
        total = 0
        while rp < n:
            total += nums[rp]
            while total >= s:
                ans = min(ans, rp - lp + 1)
                total -= nums[lp]
                lp += 1
            rp += 1

        return 0 if ans == n + 1 else ans

```


## 思路总结

双指针法，定义两个指针 start 和 end 分别表示子数组的开始位置和结束位置，维护变量 sum 存储子数组中的元素和（即从 nums[start] 到 nums[end] 的元素和）。

初始状态下，start 和 end\textit{end}end 都指向下标 0，sum 的值为 0。

每一轮迭代，将 nums[end] 加到 sum，如果 sum≥s，则更新子数组的最小长度（此时子数组的长度是 end−start+1），然后将 nums[start] 从 sum 中减去并将 start 右移，直到 sum<s，在此过程中同样更新子数组的最小长度。在每一轮迭代的最后，将 end 右移。
