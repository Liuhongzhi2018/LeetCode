# 数组中只出现一次的数字


## 题目描述

一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。


## 代码实现

1. 字典存储元素
```python
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        numsCount = {}
        numLen = len(array)
        ret = []
        for num in array:
            if num in numsCount:
                numsCount[num] += 1
            else:
                numsCount[num] = 1
        for num in numsCount:
            if numsCount[num] == 1:
                ret.append(num)
        if ret != []:
            return ret
        return 0
```
运行时间：26ms

占用内存：5712k


2.

## 思路总结

1.用字典存储数组每个数字以及出现次数，然后将出现次数为1，即键值为1的数字返回。

2。