#  和为S的两个数字


## 题目描述

输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

## 代码实现

1. 双指针法
```python
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if array is None :
            return []
        if len(array) == 0:
            return []
        i = 0
        j = len(array) - 1
        while i < j:
            if array[i] + array[j] == tsum:
                return array[i], array[j]
            elif array[i] + array[j] < tsum:
                i += 1
            else:
                j -= 1
        return []
```
运行时间：23ms

占用内存：5724k





## 思路总结

