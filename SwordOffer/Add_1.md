#  不用加减乘除做加法


## 题目描述

写一个函数，求两个整数之和，要求在函数体内不得使用+、-、* 、/四则运算符号。

## 代码实现


```python
# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            num1,num2 = (num1^num2) & 0xFFFFFFFF, ((num1&num2)<<1) & 0xFFFFFFFF
        return num1 if num1 <= 0x7FFFFFFF else ~(num1^0xFFFFFFFF)
```
运行时间：24ms

占用内存：5864k


```python
# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        xorNum = num1 ^ num2
        andNum = (num1 & num2) << 1
        while andNum:
            tmp1 = xorNum ^ andNum
            tmp2 = (xorNum & andNum) << 1
            tmp1 = tmp1 & 0xFFFFFFFF
            xorNum = tmp1
            andNum = tmp2
            
        return xorNum if xorNum <= 0x7FFFFFFF else xorNum-0x100000000
```
运行时间：28ms

占用内存：5840k



## 思路总结

（1）十进制加法分三步：(以5+17=22为例)

1. 只做各位相加不进位，此时相加结果为12(个位数5和7相加不进位是2，十位数0和1相加结果是1)；

2. 做进位，5+7中有进位，进位的值是10；

3. 将前面两个结果相加，12+10=22

（2）这三步同样适用于二进制位运算

1.不考虑进位对每一位相加。0加0、1加1结果都是0,0加1、1加0结果都是1。这和异或运算一样；

2.考虑进位，0加0、0加1、1加0都不产生进位，只有1加1向前产生一个进位。可看成是先做位与运算，然后向左移动一位；

3.相加过程重复前两步，直到不产生进位为止。

