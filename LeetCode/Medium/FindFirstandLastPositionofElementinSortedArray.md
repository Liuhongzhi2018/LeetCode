#   Find First and Last Position of Element in Sorted Array

## 问题描述

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。


## 代码实现

1.
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        if nums[right] > nums[0]:
            return nums[0]

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid]>nums[0]:
                left = mid + 1
            else:
                right = mid - 1
```


## 思考总结

二分搜索。  
一种暴力的解法是搜索整个数组，找到其中的最小元素，这样的时间复杂度是 O(N)O(N)O(N) 其中 NNN 是给定数组的大小。  
一个非常棒的解决该问题的办法是使用二分搜索。在二分搜索中，我们找到区间的中间点并根据某些条件决定去区间左半部分还是右半部分搜索。由于给定的数组是有序的，我们就可以使用二分搜索。然而，数组被旋转了，所以简单的使用二分搜索并不可行。在这个问题中，我们使用一种改进的二分搜索，判断条件与标准的二分搜索有些不同。

我们希望找到旋转排序数组的最小值，如果数组没有被旋转呢？如何检验这一点呢？如果数组没有被旋转，是升序排列，就满足 last element > first element。