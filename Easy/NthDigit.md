#  Nth Digit

## 问题分析
Find the n<sup>th</sup> digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note: n is positive and will fit within the range of a 32-bit signed integer (n < 2<sup>31</sup>).

在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。

注意: n 是正数且在32为整形范围内 ( n < 2<sup>31</sup>)。

## 代码实现
``` C
int findNthDigit(int n) {
    long long len = 1, cnt = 9, start = 1, i, cur, digit = 0;
    if( n< 10)  return n;
    while (n > len * cnt) {
        n -= len * cnt;
        len++;
        cnt *= 10;
        start *= 10;
    }
    cur = (n - 1) / len + start;  
    for (i = (n - 1) % len; i < len; i++) {
        digit = cur % 10;
        cur /= 10;
    }
    return digit;
}
```

## 总结体会

本题从1开始的整型范围内自然数序列中，要求找出第n个数字，需要注意的是如两位数是包含2个数字。

在算法设计上，应考虑两个部分，一个是确定所给第n个数字在哪个自然数序列中，二是确定在序列的第几个数字。首先用while循环确定序列，从n中分别去掉一位、两位直至多位数包含序列，从cur变量保存当前所在序列；其次采用for循环遍历序列中各位，找出第n个数字。最后返回digit即为所求数字。

