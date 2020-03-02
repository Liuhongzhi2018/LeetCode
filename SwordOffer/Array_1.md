# 二维数组中的查找


## 题目描述

在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


## 代码实现

1. 暴力查找遍历
```python

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        len1 = len(array)
        len2 = len(array[0])
        for i in range(len1):
            for j in range(len2):
                if array[i][j] == target:
                    return True
        else:
            return False
```
运行时间：224ms
占用内存：5832k


2.根据递增排序查找，先找到所在行，再按列查找
```python
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array == 0 or len(array[-1]) == 0:
            return False
        for row in array:
            if row[-1] == target:
                return True
            elif row[-1] < target:
                continue
            else:
                for col in row[:-1]:
                    if col == target:
                        return True
        return False
```

运行时间：419ms
占用内存：5708k
