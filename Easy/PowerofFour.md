#  Power of Four

## 问题分析
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Follow up: Could you solve it without loops/recursion?

给定一个整数 (32位有符整数型)，请写出一个函数来检验它是否是4的幂。

问题进阶：你能不使用循环/递归来解决这个问题吗？

## 代码实现
``` C
bool isPowerOfFour(int num) {
    if(num < 1)  return false;
    while ( num % 4 == 0) {
            num /= 4;
         if( num==0 )  return false;
        }
     return num == 1;  
}

bool isPowerOfFour(int num) {
    if(num < 1)  return false;
    if(!(num & (num - 1)) && (num - 1) % 3 == 0)  return true;
      else return false;
}

```

## 总结体会

本题要求判断所给整数是否为4的幂，即所给整数能否被4除尽。

在算法设计上，第一种方法是用常规循环判断，首先判断所给整数是否为大于0整数；其次采用while循环，若最后商为0，则一定为非4的幂；最后若商为1，则为4的幂返回true。

第二种方法不使用循环/递归来解决，只要是4的次方数，减1之后可以被3整除，一步判断出是否为4的幂。

