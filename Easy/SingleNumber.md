#  Single Number

## 问题分析
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：算法应该具有线性时间复杂度。不使用额外空间来实现。

## 代码实现
``` C
int singleNumber(int* nums, int numsSize) {
    int temp = 0;
    if (numsSize <= 0) return 0;
    for (int i = 0; i < numsSize; i++) {
        temp ^= nums[i];
    }
    return temp;
}
```

## 总结体会

本题要求数组中只出现一次的元素，而且注明算法设计具有线性时间复杂度，即一次遍历完成指定元素的筛选，时间复杂度只与数组元素个数多少有关。

因此采用按位异或的算法，出现奇数次即只出现一次的元素，保存在temp变量中返回。











