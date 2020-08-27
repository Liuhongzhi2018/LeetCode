# Base 7

## 问题描述

Given an integer, return its base 7 string representation.

给定一个整数，将其转化为7进制，并以字符串形式输出。

## 代码实现

1.
```python
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        def fun(n):
            d = ''
            while n:
                d = d + str(n % 7)
                n = (n - n%7)//7
            return d[::-1]

        if num > 0:
            return fun(num)
        else:
            return '-'+fun(abs(num))
```

## 思考总结

十进制转二进制，十进制数除7取余法，即十进制数除7，余数为权位上的数，得到的商值继续除，直到商为0为止。