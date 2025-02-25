# Remove Duplicates from Sorted Array

## 问题分析

Given a sorted array nums, 　remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, 　you must do this by modifying the input array in-place with O(1) extra memory.

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

## 代码实现

1.
``` C
int removeDuplicates(int* nums, int numsSize)
{
	int i = 0;
	int j = 1;
	if (numsSize == 0)  return 0;
	printf("%d", *nums);
	while (j < numsSize)
	{
		if (nums[i] == nums[j])
		{
			j++;
		}
		else
		{
			nums[++i] = nums[j++];
			printf(",%d", nums[i]);
		}
	}
	return i + 1;
}
```

2.遍历元素
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        for num in nums:
            if nums[res] != num:
                res += 1
                nums[res] = num
        return res+1
```

3.双指针法
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nlen = len(nums)
        if not nlen:
            return 0
        lp, rp = 0, 0
        while rp < nlen:
            if nums[lp] != nums[rp]:
                lp += 1
                nums[lp] = nums[rp]
            rp += 1
        return lp+1
```

## 总结体会

本题考察对数组元素的操作和删除，我认为主要难点在于in-place和O(1)的要求，即要求数组的多余元素一次删除完成。

采用的方法是使用两个变量，一个指向当前元素，一个向后寻找，遇到重复的元素则跳过，使数组依次存储不同的元素，实现题目要求。

思路是用下标保存不重复的元素，然后返回下标+1即可。

双指针法：  
左指针用于保存当前不重复的元素下标，右指针从左向右遍历列表，每一个元素都与当前元素比较，如果不同则移动左指针，将不同元素保存在当前位置。
