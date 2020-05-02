#  Valid Perfect Square

## 问题分析
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

注意：不要使用任何内置的库函数，如 sqrt。

## 代码实现
``` C
bool isPerfectSquare(int num) {
    int i;
    if (num< 1)  return false;
    if (num == 1) return true;
    for (i = 1; i <= num / 2; i++) {
        if (i * i == num)
            return true;
    }
    return false;
}
```

## 总结体会

本题要求判断所给正整数是否为完全平方数，即是否可以找到一个数的平方是所给整数。

算法设计上，采用for循环，从1开始进行遍历判断直到所给整数的一半，每次进行平方后与所给整数比较，如果找到符合条件的整数，返回true，否则false。

