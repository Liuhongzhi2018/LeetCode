#  二进制中1的个数


## 题目描述

输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。


## 代码实现

1. 字符串法
```python
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        n = n & 0xFFFFFFFF
        count = 0
        for c in str(bin(n)):
            if c == "1":
                count += 1
        return count 
```

运行时间：23ms

占用内存：5856k

2.掩码法
```python
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        n = n & 0xFFFFFFFF
        count = 0
        for i in range(32):
            mask = 1 << i
            if n & mask != 0:
                count += 1
        return count
```
运行时间：21ms

占用内存：5988k

3.掩码法
```python
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        while n:
            n = n&(n-1)
            count += 1
            n = 0xFFFFFFFF & n
        return count
```
运行时间：22ms

占用内存：5724k


## 思路总结

对二进制数取32位。  
补码：正数不变，负数是它正数的反码+1

二进制时，n-1使末尾0变1，1变0。