# Remove Duplicates from Sorted Array

## 问题分析
Given a sorted array nums, 　remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, 　you must do this by modifying the input array in-place with O(1) extra memory.

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

## 代码实现
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

## 总结体会
本题考察对数组元素的操作和删除，我认为主要难点在于in-place和O(1)的要求，即要求数组的多余元素一次删除完成。

采用的方法是使用两个变量，一个指向当前元素，一个向后寻找，遇到重复的元素则跳过，使数组依次存储不同的元素，实现题目要求。
