#  Contains Duplicate

## 问题分析
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回true。如果数组中每个元素都不相同，则返回false。


## 代码实现
``` C
bool containsDuplicate(int* nums, int numsSize) {
    int n = numsSize;
    if (n <= 1) return false;
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = i+1; j < n; j++) {
            if (nums[i] == nums[j])  return true;
        }
    }
    return false;
}
```

## 总结体会

本题要求判断在给定的整数数组中是否存在重复元素。

采用的算法比较简单，首先分别用i和j变量保存数组元素。其次用i遍历所有数组元素，用j从i后元素开始遍历，如果i与j相等，即为重复元素，返回true。否则没有满足条件的元素，返回false。