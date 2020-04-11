# 斐波那契数列


## 题目描述

大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39 


## 代码实现

1. 循环法
```python
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n
        count = n - 1
        n1 = 0
        n2 = 1
        while count:
            num = n1 + n2
            count -= 1
            n1,n2 = n2,num
        return num
```
运行时间：23ms

占用内存：5864k

```
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n
        count = n - 1
        n1 = 0
        n2 = 1
        for i in range(2,n+1):
            num = n1 + n2
            count -= 1
            n1,n2 = n2,num
        return num
```


2.递归法
```python
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        assert n >= 0, "n > 0"
        if n <= 1:
            return n
        return self.Fibonacci(n-1) + self.Fibonacci(n-2)
```
时间复杂度太大，不能在规定时间运行完成。

写法最简洁，但是效率最低，会出现大量的重复计算，时间复杂度O(1.618^n)，而且最深度1000。
