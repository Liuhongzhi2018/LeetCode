# 旋转数组的最小数字


## 题目描述

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。

例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。

NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。


## 代码实现

1. 擂台算法
```python
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        rlen = len(rotateArray)
        if rlen == 0:
            return 0
        min = rotateArray[0]
        for i in range(rlen):
            cur = rotateArray[i]
            if cur < min:
                min = cur
        return min
```
运行时间：1503ms

占用内存：5708k


2. 三目运算符
```python
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        rlen = len(rotateArray)
        minNum = 0
        for i in range(rlen):
            minNum = minNum if minNum < rotateArray[i] and minNum != 0 else rotateArray[i]
        return minNum
```
运行时间：1199ms

占用内存：5840k


3. 二分查找法
```python
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        left = 0
        right = len(rotateArray) - 1
        while left <= right:
            mid = (left + right) // 2
            if rotateArray[mid] < rotateArray[mid-1]:
                return rotateArray[mid]
            elif rotateArray[mid] < rotateArray[right]:
                right = mid - 1
            else:
                left = mid + 1
        return 0
```
运行时间：679ms 

占用内存：5728k


## 思路总结

1. 逐次比较，从数组中找到最小值。

2. 二分查找，最小值前会出现断崖下降，即顺序上后面值小于前面值。先找到中间值，和前面值比较，如果小则满足，否则调整范围继续查找。