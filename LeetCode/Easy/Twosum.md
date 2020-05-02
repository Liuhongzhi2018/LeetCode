# Two sum

## 问题分析
给定一个整数数列，找出其中和为特定值的那两个数。
你可以假设每个输入都只会有一种答案，同样的元素不能被重用。

## 编程实现
``` C
int* twoSum(int* nums, int numsSize, int target) {  
   int n = numsSize;  
   int sum = target;  
   for (int i = 0; i < n-1; i++)  
	{  
	for (int j = i + 1; j < n ; j++)  
	    if (nums[i] + nums[j] == sum)  
		cout<<"[ "<<i<<" , "<<j<<" ] "<<endl;
	}  
    return 0;  
}
```
