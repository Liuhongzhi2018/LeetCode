#  Missing Number

## 问题分析
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

## 代码实现
``` C
int missingNumber(int* nums, int numsSize) {
    int i,n;
    int missing=0;
    n=numsSize;
    for(i=0;i<n;i++)
        missing ^=((i+1)^nums[i]);
    return missing;
}
```

## 总结体会

本题要求找出从0开始的常数列中，没有出现在序列中的数字。

在算法设计上，采用异或运算方法，若给定的数组缺失一个数字，那么对数组所有元素和不缺失的情况中所有元素进行异或操作，则可以得到缺失的那个数字。