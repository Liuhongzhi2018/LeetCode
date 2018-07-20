# Two Sum

## 问题分析
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。


## 代码实现
``` C
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int i,j;
    int *a = (int*)malloc(sizeof(int)*2);
    for(i = 0;i<numsSize;i++){
        for(j = i+1;(j<numsSize && j != i);j++){
            if(nums[i] + nums[j] == target){
                a[0] = i;
                a[1] = j;
            }
        }
    }
    return a;
}
```

## 总结体会
本题要求从给定的数组中，找到相加和与目标值相等的两个数返回，根据题意只要求返回一种答案。

在算法设计上，采用for循环嵌套，用i和j两个下标，对数组元素进行遍历，i指向当前元素，j指向i后的元素，判断和与目标值是否一致，如果满足则返回i和j，即为所求的一种答案。