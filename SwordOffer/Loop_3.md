#  变态跳台阶


## 题目描述

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

## 代码实现

1. 循环法
```python
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        count = 1
        a = 1
        for i in range(2, number + 1):
            count = 2 * a
            a = count 
        return count
```
运行时间：26ms

占用内存：5856k




## 思路总结

注意找规律。

f(n) = f(n-1) + f(n-2) + ... + f(1) = f(n-1)+f(n-1) = 2 * f(n-1)