#  Power of Three

## 问题分析

Given an integer, write a function to determine if it is a power of three.

给定一个整数，写一个函数来判断它是否是 3 的幂次方。

## 代码实现

1.
``` C
bool isPowerOfThree(int n) {
    if(n < 1)  return false;
    while ( n % 3 == 0) {
            n /= 3;
         if( n==0 )  return false;
        }
     return n == 1;  
}
```

2.
```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0: 
            return False 
        while n != 1: 
            if n % 3 != 0 : 
                return False 
            n = n // 3 
        return True
```

## 总结体会

本题要求判断所给整数是否为3的幂，即所给整数能否被3除尽。

在算法设计上，首先判断所给整数是否为大于0整数；其次采用while循环，若最后商为0，则一定为非3的幂；最后若商为1，则为3的幂返回true。

方法二是n除以3，看是否有余数，如果有就直接为False，否则就递归继续，直到3除以3等于1时候返回TRUE。
注意：本题人为1也为TRUE。
