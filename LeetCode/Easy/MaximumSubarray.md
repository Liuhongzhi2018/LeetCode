# Maximum Subarray

## 问题分析
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

给定一个整数数组nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

## 代码实现
``` C
int maxSubArray(int* nums, int numsSize) {
    int sum = 0;
	int max = nums[0];
	if (numsSize <= 0)  return 0;
	for (int i = 0; i<numsSize; i++) {
		sum += nums[i];
		if (sum<0) {
			max = (max>sum) ? max : sum;
			sum = 0;
			continue;
		}
		max = (max>sum) ? max : sum;
	}
	return max;
}
```

## 总结体会

本题寻找连续子序列和的最大值，可以采用遍历查找的算法实现。
将数组元素和保存到sum变量中，每完成一次元素之和，与max保存的最大值进行比较，如果小于max值，则max值不变，否则更新为sum值，最后返回最大和max值。
