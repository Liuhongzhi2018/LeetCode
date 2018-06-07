#  Ugly Number

## 问题分析
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

## 代码实现
``` C
bool isUgly(int num) {
    if (num < 1) return false;
    if (num == 1) return true;
    int i;
    for (i = 2; i < 6; i++) {
        while (num%i == 0) {
            num /= i;
        }
    }
    return num == 1;
}
```

## 总结体会

本题主要判断给定的一个数是否为丑数，丑数满足只包含质因数2、3和5的正整数，并且1为丑数。

在算法设计上，首先判断所给数是否为正整数，若不是则返回false；其次进入循环判断，依次进行2、3和5的质因数循环相除，用i作为变量，如果仅含2、3和5质因数，则num终为1，否则跳出循环体后num不为1。最后返回num==1的条件判断表达式，如果满足则为符合要求的丑数。