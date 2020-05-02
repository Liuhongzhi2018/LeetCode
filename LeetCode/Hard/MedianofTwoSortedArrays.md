#   Median of Two Sorted Arrays

## 问题分析

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。


## 代码实现


1.
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        i = len(nums3) // 2
        j = len(nums3) // 2 - int(len(nums3)%2==0)
        return (nums3[i]+nums3[j]) / 2
```

2.
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            # swap 减少二分查找需要的查询次数
        m, n = len(nums1), len(nums2)
        mark = (m+n-1) // 2

        l,r = 0, m
        while l<r:
            mid = (l + r) //2
            if mark-mid-1< 0 or nums1[mid]>=nums2[mark-mid-1]:
                r = mid
            else:
                l = mid + 1

        middlepoints = sorted(nums1[l:l+2] + nums2[mark-l:mark-l+2])
        return (middlepoints[0]+middlepoints[1-(m+n)%2]) / 2.0

```

## 思路总结

总共有(m+n)个元素，根据中位数的性质，我们如果可以把元素分为大致相等的两堆，可以快速找出中位数。  
具体来说，总的元素个数是(m+n)个，被分到小堆的个数是(m+n-1)/2向下取整，被分到大堆的是剩下的元素。  
情形1：(m+n)是奇数，(m+n-1)/2使得小堆元素比大堆少1个；  
情形2：(m+n)是偶数，(m+n-1)/2向下取整等于(m+n-2)/2，使得小堆元素比大堆少2个。

具体实现的时候，我们通过二分查找法，寻找nums1中需要被分配到小堆的切分点——关键点：  
1. 在前面通过计算可以得到小堆应有的元素个数(m+n-1)//2；  
2. 通过确定nums1中被分到小堆的个数，可以轻易计算出nums2中被分到小堆的个数。