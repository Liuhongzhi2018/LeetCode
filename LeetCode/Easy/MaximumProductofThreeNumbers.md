# Maximum Product of Three Numbers  

## 问题描述

Given an integer array, find three numbers whose product is maximum and output the maximum product.

给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

## 代码实现

1.滑动窗口
```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums_sorted=sorted(nums) 
        result=[] 
        
        for i in range(len(nums)): 
            if i<len(nums)-2: 
                result.append(nums_sorted[i]*nums_sorted[i+1]*nums_sorted[i+2]) 
            elif i==len(nums)-2: 
                    result.append(nums_sorted[i]*nums_sorted[i+1]*nums_sorted[0]) 
            else: result.append(nums_sorted[i]*nums_sorted[0]*nums_sorted[1]) 
        return max(result)
```

2.
```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        l = sorted(nums, reverse=True)
        return max(l[0]*l[1]*l[2], l[-1]*l[-2]*l[0])
```

## 思考总结

1.排序
2.两种情况，3正[0,1,2]和2正1负[0,-1,-2]