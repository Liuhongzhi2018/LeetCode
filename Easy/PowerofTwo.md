#  Power of Two

## 问题分析
Given an integer, write a function to determine if it is a power of two.

给定一个整数，写一个函数来判断它是否是 2 的幂次方。


## 代码实现
``` C
bool isPowerOfTwo(int n) {
     int end = 0;
        while (n > 0) {
            end += (n & 1);
            n >>= 1;
        }
        return end == 1;
} 
```

## 总结体会

本题要求判断给定整数是否为2的幂。

算法设计上首先将末位赋值为0，判断最低位是否为1，然后向右移1位进行位运算，最后统计1的个数即可判断给定整数是否为2的幂。