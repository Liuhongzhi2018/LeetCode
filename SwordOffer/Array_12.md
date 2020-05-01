# 把数组排成最小的数

## 题目描述

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

## 代码实现

1. 
```python
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if numbers is None or len(numbers) == 0: 
            return "" 
        numbers = map(str, numbers) 
        numbers.sort(cmp = lambda x, y : cmp(x + y, y + x)) 
        return "".join(numbers).lstrip()
```
运行时间：22ms

占用内存：5756k



## 思路总结

先将整数数组转为字符串数组，然后用比较器实现字符串比较大小。如果有字符串A和B， A + B < B + A，则A在前；反之B在前。最后将字符串数组连接去除返回值左侧