# 数组中出现次数超过一半的数字


## 题目描述

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。



## 代码实现

1. 字典保存键值
```python
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        numsCount = {}
        numLen = len(numbers)
        for num in numbers:
            if num in numsCount:
                numsCount[num] += 1
            else:
                numsCount[num] = 1
            if numsCount[num] > (numLen >> 1):
                return num
        return 0
```
运行时间：25ms

占用内存：5860k

2. 抵消法
```python
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        last = 0
        count = 0
        for num in numbers:
            if count == 0:
                last = num
                count = 1
            else:
                if num == last:
                    count += 1
                else:
                    count -= 1
        if count == 0:
            return 0
        else:
            count = 0
            for num in numbers:
                if num == last:
                    count += 1
            if count > (len(numbers)>>1):
                return last
        return 0
```
运行时间：21ms

占用内存：5860k


## 思路总结

1. 将数组的元素和个数保存为键值对，通过对键值判断，返回满足条件的键，即为所求数字。  
时间复杂度O(n)，空间复杂度O(n)。

2.遇到不相同的数字，就相互抵消掉，最终剩下的数字就可能是大于一半的数字。
时间复杂度O(n)，空间复杂度O(1)。