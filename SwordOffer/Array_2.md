# 数组中重复的数字 


## 题目描述

在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。


## 代码实现

1. 字典查找法
```python
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        dict = {} 
        for num in numbers: 
            if num not in dict: 
                dict[num] = 0 
            else: 
                duplication[0] = num 
                return True
        return False
```
运行时间：25ms
占用内存：5640k

2. 下标计数器法
```python
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        count = [0 for _ in range(len(numbers))]
        for num in numbers:
            count[num] += 1
            if count[num] > 1:
                duplication[0] = num
                return True
        return False

```
运行时间：30ms
占用内存：5640k


3. 下标计数器法
```python
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        long = len(numbers) 
        for i in range(len(numbers)): 
            index = numbers[i]%long if numbers[i] >= long  else numbers[i] 
            if numbers[index] > long: 
                duplication[0] = index 
                return True 
            numbers[index] += long 
        return False
```
运行时间：26ms
占用内存：5724k


## 思路总结
1. 字典查找法，是将遇到的元素保存在字典中，如果再遇到相同的元素则返回第一个重复的元素；
2. 下标计数器法，是定义一个等长的列表，出现一个数字则在对应相同下标位置元素值加一，当大于1时则该下标对应的元素重复；
3. 利用现有数组设置标志，当一个数字被访问过后，可以设置对应位上的数 + n，之后再遇到相同的数时，会发现对应位上的数已经大于等于n了，那么直接返回这个数即可。