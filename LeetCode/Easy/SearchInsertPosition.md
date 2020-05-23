# Search Insert Position    

## 问题分析

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

## 代码实现

1.
``` C
int searchInsert(int* nums, int numsSize, int target) {
    int *a = nums;
	int n = numsSize;
	int m = target;
	for (int i = 0; i < n;i++) {
		if (m <= a[i])
			return i;
	}
	return n;
}
```

2.
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid +1 
            elif nums[mid]>target:
                r = mid -1
            else:
                return mid
        return l
```


## 总结体会

本题算法比较简单，将目标元素与数组元素比较，如果小于或者等于则返回数组元素位置，即可实现题目要求，一次编译通过。

实际上实现python的bisect包的bisect_left函数功能，即二分查找。首先初始化左右指针l和r，然后计算中间点，当中间点小于target时修改左指针，否则修改右指针。最后返回l即可。