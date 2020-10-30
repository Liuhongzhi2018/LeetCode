#  Subarray Sum Equals K

## 问题描述

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。


## 代码实现

1.Hashmap哈希表
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Hash = {0:1} 
        numSum = 0 
        res = 0 
        for i in range(len(nums)): 
            numSum += nums[i] 
            res += Hash.get(numSum-k, 0) 
            Hash[numSum] = Hash.get(numSum, 0) + 1
        return res
```


## 思路总结

利用哈希表记录前缀和可以巧妙地用空间兑换时间：不难发现sum[i:j] = sum[0:j] - sum[0:i]，不妨将sum[i:j]设为k，于是可以转化为sum[0:j] - k = sum[0:i]，我们可以实时记录前缀和的频数，并实时查找是否前面存在与sum[0:j]-k相等的前缀和，若能查询到，则将频数加总到结果当中。