#  Move Zeroes

## 问题分析
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note: You must do this in-place without making a copy of the array. Minimize the total number of operations.


给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

说明: 必须在原数组上操作，不能拷贝额外的数组。尽量减少操作次数。

## 代码实现
``` C
void moveZeroes(int* nums, int numsSize) {
    int i, j = 0, n = numsSize;
    for (i = 0; i < n; i++) {
        if (nums[i])
            nums[j++] = nums[i];
    }
    for (j; j < n; j++)
        nums[j] = 0;
}
```

## 总结体会

本题要求在给定数组保持非零元素相对顺序不变的前提下，将所有0元素移动到末尾，实际上是依次找到非零元素并将其从头开始放入数组中。

在算法设计上，首先遍历数组元素，在原数组中若非零，则挑选出来在数组中重新排列出来。其次将数组后面剩余位置补零，得到的数组即为排列要求的数组。满足在原数组操作且操作次数较少的题目说明要求，复杂度主要取决于非零元素个数，第一次OJ可以Accepted。