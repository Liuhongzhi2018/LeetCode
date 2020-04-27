#  矩形覆盖


## 题目描述

我们可以用2 * 1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2 * 1的小矩形无重叠地覆盖一个2 * n的大矩形，总共有多少种方法？ 

## 代码实现

1. 循环法
```python
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        
        if number == 0 or number == 1 or number == 2:
            return number
        a = 1
        b = 2
        for i in range(3, number + 1):
            b = a + b
            a = b - a
            
        return b
```
运行时间：23ms

占用内存：5848k





## 思路总结

参考斐波那契数列解法，放第一块有2种情况

f(n) = f(n-1) + f(n-2)