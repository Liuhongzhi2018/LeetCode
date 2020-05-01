#  求1+2+3+...+n


## 题目描述

求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

## 代码实现

1. 递归法
```python
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        ans = (n>0) and n
        return ans and self.Sum_Solution(n-1)+ans
```
运行时间：32ms

占用内存：5756k






## 思路总结

使用递归f(n) = f(n-1) + n， 但是不能使用if进行递归出口的控制，因此利用python中and的属性，即and判断都为真的话输出and后面的那个数字