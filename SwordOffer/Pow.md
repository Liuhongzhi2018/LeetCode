#  数值的整数次方


## 题目描述


给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

保证base和exponent不同时为0



## 代码实现

1. 
```python
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        elif exponent > 0:
            ans = 1.0
            for i in range(exponent):
                ans *= base
            return ans
        else:
            ans = 1.0
            a = abs(exponent)
            for i in range(a):
                ans *= base
            ans = 1 / ans
            return ans
```
运行时间：29ms

占用内存：5868k



## 思路总结

