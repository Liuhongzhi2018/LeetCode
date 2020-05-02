#  Rotate Array

## 问题分析
Given an array, rotate the array to the right by k steps, where k is non-negative.

Note: Do it in-place with O(1) extra space.

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

说明: 要求使用空间复杂度为 O(1) 的原地算法。


## 代码实现
``` C
void rotate(int* nums, int numsSize, int k) {
    int n = numsSize;
    if (n <= NULL)  
        printf("%d",NULL);
    int i,j,temp;
    for (i = 0; i<k; i++) {
        temp = nums[n - 1];
        for (j = n - 1; j>0; j--)
            nums[j] = nums[j - 1];
        nums[0] = temp;
    }
    for (i = 0; i < n; i++) {
        printf("%d", nums[i]);
    }
}
```

## 总结体会

本题求旋转数组，可以看成求一个循环队列，即一个首尾相接的圆环，当起点不同时数组元素的排列顺序。

算法设计上，采用for循环嵌套，内部for循环完成末尾元素移动到第一个元素位置，原第一个元素向后移一位。外部for循环决定了移动的次数，即完成K次移动操作，用temp保存末尾元素。