# 调整数组顺序使奇数位于偶数前面


## 题目描述

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。


## 代码实现

1. 列表拼接
```python
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        evenlist = []
        oddlist = []
        for i in array:
            if i % 2 == 1:
                oddlist.append(i)
            else:
                evenlist.append(i)
        oddlist += evenlist
        return oddlist
```
运行时间：29ms

占用内存：5860k


2. 冒泡排序法



## 思路总结

1. 声明2个列表，分别保存奇数和偶数，然后对两个列表拼接。