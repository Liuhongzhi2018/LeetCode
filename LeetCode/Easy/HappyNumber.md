#  Happy Number

## 问题分析
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。


## 代码实现
``` C
int Square(int m) {
    int temp;
    int sum=0;
    while (m) {
        temp = m % 10;
        sum += temp*temp;
        m /= 10;
    }
    return sum;
}

bool isHappy(int n) {
    int pre, next;
    pre = next = n;
    do {
        pre = Square(pre);
        next = Square(next);
        next = Square(next);
    } while (pre != next);
    if (pre == 1)  return true;
    else return false;
}
```

## 总结体会

本题要求判断快乐数，可转化为循环求各个位平方和是否最后为1的判断要求。

算法设计上，用Square函数计算各个位数字的平方和，进行的是取余平方求和再除10判断再循环的过程。在isHappy函数中，pre为前向变量，next为后向变量且步进比pre多1，这样pre与next终会相等。如果满足Happy数条件，最终pre和next将均与1相等，返回true；否则pre与next相等时不为1，则不满足Happy数条件，返回false。