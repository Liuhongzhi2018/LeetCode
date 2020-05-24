#   First Missing Positive

## 问题分析

Given an unsorted integer array, find the smallest missing positive integer.

给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

提示：

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。

## 代码实现

1.
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums += [2**31]*2
        for i in range(len(nums)):
            if nums[i]<0 or nums[i]>=len(nums):
                nums[i] = 0
        
        for i in range(len(nums)):
            cur = abs(nums[i])
            if nums[cur] == 0:
                nums[cur] = -cur
            else:
                nums[cur] = -1 * abs(nums[cur])
        
        for i in range(1,len(nums)):
            if nums[i] >= 0:
                return i
```


## 思路总结

首先由于数组长度为n，所以答案一定在[1,n+1]之中出现，所以第一轮把无关项全部剔除改为0；  
需要给数组长度为n的数组加上2个尾部元素(2^31)，因为该元素的下标为n，而我们需要记录一直到n+1的，所以添加两个元素； 
第二轮遍历，因为现在数字的范围是在[0,n+1]中，可以想一个办法在原数组中标记出现过的n；  
标记方法是将出现过的k的下标位置的元素变为负数，以此标记出现过的k； 
第三轮遍历下标，从1开始到n+1结束，当有元素是大于等于0时，返回当前下标。
