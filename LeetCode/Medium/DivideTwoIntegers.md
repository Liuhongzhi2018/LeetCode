#  Divide Two Integers

## 问题分析

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

## 代码实现

1.
``` C++
class Solution {
public:
    int divide(int dividend, int divisor) {
        int n,sign = 1; 
        if ((dividend >0 && divisor < 0) || (dividend < 0 && divisor >0)){ 
            sign = -1; 
        } 
        unsigned int left = dividend > 0 ? dividend : -dividend; 
        unsigned int right = divisor > 0 ? divisor : -divisor; 
        unsigned reslut = 0; 
        while (left >= right) { 
            n = 1; 
            unsigned temp = right; 
            while (left>= temp) { 
                left -= temp; 
                reslut += n; 
                if (temp < (INT32_MAX >> 1)){
                    temp = temp << 1;
                    n = n << 1;
                } 
            } 
        }
        if (reslut > INT32_MAX && sign >0){
            return INT32_MAX; 
        }
        return sign * reslut; 
    }
};
```

2.
```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        limit = 2**31
        isNeg = (dividend<0)!=(divisor<0)
        dividend, divisor = abs(dividend),abs(divisor)
        res = 0
        div, track = divisor,1
        while dividend >= divisor:
            while dividend >= (div<<1):
                div <<= 1
                track <<= 1
            res += track
            dividend -= div
            div, track = divisor,1
        return max(-limit,min(limit-1,-res if isNeg else res))
```

## 总结体会

本题要求实现除法运算，不使用乘法、除法和求余 算术运算符，已知有符号整数的位数，以及溢出时返回数值。

在算法设计上，首先用变量sign保存符号位，同号为1异号为-1，并将被除数和除数转换为正数；其次从被除数中减去若干倍数的除数，用位运算使每次减去的除数增大；最后result即为所求正数相除的商，再乘符号位即为所求结果。

此题只能考虑加法，减法和位移，加减法时间不满足要求，选择位移的方式；  
将十进制转换为二进制，左移div得到不大于dividend的最大二进制，dividend减div得到新被除数，更新div和track。

首先声明一个limit，用于题目条件，isNeg用于判断结果是否为负数；然后将除数和被除数转换为绝对值的形式；其次用res来存储结果，用div做一个变换，而track是用于叠加结果。