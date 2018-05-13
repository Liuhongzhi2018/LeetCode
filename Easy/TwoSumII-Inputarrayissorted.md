#  Two Sum II - Input array is sorted

## 问题分析
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Notes:

* Your returned answers (both index1 and index2) are not zero-based.
* You may assume that each input would have exactly one solution and you may not use the same element twice.

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

* 返回的下标值（index1 和 index2）不是从零开始的。
* 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

## 代码实现
``` C
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int i, j;
    int n = numbersSize;
    *returnSize = 2;
    int *a = (int*)malloc(sizeof(int) * 2);
    for (i = 0; i<n-1; i++) {
        for (j = i + 1; j<n; j++) {
            if (numbers[i] + numbers[j] == target) {
                 *a = i + 1;
                 *(a+1) = j + 1;
                 break;
             }
        }
    }
    return a;
}
```

## 总结体会

本题要求从数组中找到两个数相加之和等于目标数，在实际算法设计上是否为有序数组并不影响，即乱序数组的复杂度与有序数组一样。

算法设计上采用双指针的for循环嵌套，当数组中两元素之和等于目标数时，将对应下标返回。需要注意的是，由于例子中，下标是从0开始，在向returnSize数组返回时，需要将数组下标+1，返回值才符合题目要求。











