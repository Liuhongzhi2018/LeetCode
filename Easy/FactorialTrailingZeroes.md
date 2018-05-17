#  Factorial Trailing Zeroes

## 问题分析
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

给定一个整数 n，返回 n! 结果尾数中零的数量。

说明: 算法的时间复杂度应为 O(log n) 。

## 代码实现
``` C
int trailingZeroes(int n) {
     int num = 0;
        while (n > 0) {
            num += n / 5;
            n /= 5;
        }
        return num;
}
```

## 总结体会

本题要求任意数的阶乘结果中尾数零的个数，利用质因数分解可以将n的阶乘看成多个质因数的幂相称的结果，其中，只有2和5相乘才会出现10，增加1个末尾零，因为2的个数远大于5，所以求末尾0的个数问题就转化为求n!中5的个数。

算法设计上采用while循环，num为质因数中5的个数，num每保存一次，给定整数值除5直至为零，返回num值。












