#  Pow(x, n)

## 问题分析

Implement pow(x, n), which calculates x raised to the power n(x<sup>n</sup>).

实现 pow(x, n) ，即计算 x 的 n 次幂函数。

## 代码实现

1.
``` C++
class Solution {
public:
    double myPow(double x, int n) {
      if(n<0) return 1.0/newpow(x,-n);
      else return newpow(x,n);
    }
    double newpow(double x,int n){
        if(n==0) return 1.0;
        double y=newpow(x,n/2);
        if(n&1) return y*y*x;
        else return y*y;
    }
};
```

2.递归法
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:  
            return 1
        #若为负数
        if n<0:  
            return 1.0/self.myPow(x,-n)
        #若n为奇数
        if n%2==1:  
            return x*self.myPow(x*x,n//2)  
        else:  
            return self.myPow(x*x,n//2) 
```

## 总结体会

本题要求代码实现x的幂运算过程。

在算法设计上，首先判断指数是否为正；其次采用递归思想和二分法，将幂运算转化为乘积运算；最后返回乘积值即为所求的幂。
