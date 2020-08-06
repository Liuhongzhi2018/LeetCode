#  Sum of Square Numbers

## 问题分析

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a × a + b × b = c.

给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a × a + b × b = c。

## 代码实现
1.
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

2.双指针法
```python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        a, b = 0, int(sqrt(c))
        while a <= b:
            if a * a + b * b == c:
                return True
            elif a * a + b * b > c:
                b -= 1
            elif a * a + b * b < c:
                a += 1
            else:
                return False
```

## 总结体会

本题要求不使用加减运算符实现加减运算，实质是了解计算机内部如何进行加减运算过程的。

模二加法是一种二进制的运算，等同于“异或”运算。规则是两个序列按位相加模二，即两个序列中对应位，相加，不进位，相同为0，不同为1。本题算法采用a ^ b 直接算出a + b 每位上模2的结果，进位是直接 (a & b)左移一位得到。

双指针法，左指针从0开始，右指针从所给数的平方根开始，循环结束条件时左指针不大于右指针。右指针以平方根值初始化，实现剪枝，降低时间复杂度。

