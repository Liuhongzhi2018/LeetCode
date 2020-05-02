#  Sum of Two Integers

## 问题分析
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

不使用运算符 + 和-，计算两整数a 、b之和。

## 代码实现
``` C
int getSum(int a, int b) {
    int c;    
    while (b != 0) {
            c = a & b;
            a ^= b;
            b = c << 1;
        }
        return a;
}
```

## 总结体会

本题要求不使用加减运算符实现加减运算，实质是了解计算机内部如何进行加减运算过程的。

模二加法是一种二进制的运算，等同于“异或”运算。规则是两个序列按位相加模二，即两个序列中对应位，相加，不进位，相同为0，不同为1。本题算法采用a ^ b 直接算出a + b 每位上模2的结果，进位是直接 (a & b)左移一位得到。

