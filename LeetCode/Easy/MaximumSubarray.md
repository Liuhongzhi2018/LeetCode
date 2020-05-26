# Maximum Subarray

## 问题分析

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

给定一个整数数组nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

## 代码实现

1.
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

2. 遍历法
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #onesum维护当前的和
        onesum = 0
        maxsum = nums[0]
        for i in range(len(nums)):
            onesum += nums[i]
            maxsum = maxsum if maxsum > onesum else onesum
            #出现onesum<0的情况，就设为0，重新累积和
            if onesum < 0:
                onesum = 0
        return maxsum
```

3. 分治递归
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #主函数
        left = 0
        #左右边界
        right = len(nums)-1
        #求最大和
        maxSum = self.divide(nums,left,right)
        return maxSum
     
    def divide(self,nums,left,right):
        #如果只有一个元素就返回
        if left==right:
            return nums[left]
        #确立中心点
        center = (left+right)//2
        #求子序在中心点左边的和
        leftMaxSum = self.divide(nums,left,center)
        #求子序在中心点右边的和
        rightMaxSum = self.divide(nums,center+1,right)
        
        #求子序横跨2边的和，分成左边界和和右边界和
        leftBorderSum = nums[center]
        leftSum = nums[center]
        for i in range(center-1,left-1,-1):
            leftSum += nums[i]
            if leftSum>leftBorderSum:
            #不断更新左区块的最大值
                leftBorderSum = leftSum
        
        rightBorderSum = nums[center+1]
        rightSum = nums[center+1]
        for i in range(center+2,right+1):
            rightSum += nums[i]
            if rightSum>rightBorderSum:
            #不断更新右区块的最大值
                rightBorderSum = rightSum
        #左边界的和 + 右边那块的和
        BorderSum = leftBorderSum + rightBorderSum
        return max(leftMaxSum,rightMaxSum,BorderSum)
```

## 总结体会

本题寻找连续子序列和的最大值，可以采用遍历查找的算法实现。
将数组元素和保存到sum变量中，每完成一次元素之和，与max保存的最大值进行比较，如果小于max值，则max值不变，否则更新为sum值，最后返回最大和max值。

遍历法：遍历数组，用onesum去维护当前元素加起来的和。当onesum出现小于0的情况时，我们把它设为0。然后每次都更新全局最大值。

分治递归法：分治法，最大子序和要么在左半部分，要么在右半部分，要么就横跨两部分（即包括左半部分的最后一个元素，和右半部分的第一个元素）。返回这三种情况的最大值即可。第三种情况，其中包括左半部分最后一个元素的情形，需要挨个往前遍历，更新最大值。包含右半部分的第一个元素的情况类似。总的时间复杂度O(nlogn)。