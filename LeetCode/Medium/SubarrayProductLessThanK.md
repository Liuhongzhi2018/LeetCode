#  Subarray Product Less Than K

## 问题描述

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

给定一个正整数数组 nums。

找出该数组内乘积小于 k 的连续的子数组的个数。


## 代码实现

1.双指针
```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prob = 1
        ret = lp = 0
        for rp, val in enumerate(nums):
            prob *= val
            while prob >= k:
                prob /= nums[lp]
                lp += 1
            ret += rp - lp + 1
        return ret
```


## 思路总结

双指针算法分析  
对于每个 right，我们需要找到最小的 left，满足 i=\mathrm{left}}^\mathrm{right} \mathrm{nums}[i] < k。由于当 left 增加时，这个乘积是单调不增的，因此我们可以使用双指针的方法，单调地移动 left。

算法  
我们使用一重循环枚举 right，同时设置 left 的初始值为 0。在循环的每一步中，表示 right 向右移动了一位，将乘积乘以 nums[right]。此时我们需要向右移动 left，直到满足乘积小于 k 的条件。在每次移动时，需要将乘积除以 nums[left]。当 left 移动完成后，对于当前的 right，就包含了 right−left+1个乘积小于 k 的连续子数组。