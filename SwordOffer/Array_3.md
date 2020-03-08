# 构建乘积数组


## 题目描述


给定一个数组 <img src="http://latex.codecogs.com/gif.latex?1+sin(x)" border="0"/>  A[0,1,...,n-1] ,请构建一个数组 B[0,1,...,n-1] ,其中B中的元素 B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。（注意：规定 B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）


## 代码实现

1. 两层for循环
```python
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = []
        for num in range(len(A)):
            val = 1
            for i in range(len(A)):
                if i != num:
                    val *= A[i]
            B.append(val)
        return B
```
运行时间：26ms

占用内存：5652k

1. 分两部分，三角形求解
```python
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        n = len(A)
        B = [1 for i in range(n)]
        # top-down
        for j in range(1,n):
            B[j] = B[j-1] * A[j-1]
        tmp = 1
        # down-top
        for j in range(n-2,-1,-1):
            tmp *= A[j+1]
            B[j] *= tmp
        return B
```
运行时间：24ms

占用内存：5836k




## 思路总结
1. 两层for循环，时间复杂度O(n^2)；

2.第一步：计算左下三角，也就是每行的【】之前的乘积

第一步：b[0] = 1;
第二步：b[1] = b[0] * a[0] = a[0]
第三步：b[2] = b[1] * a[1] = a[0] * a[1];
第四步：b[3] = b[2] * a[2] = a[0] * a[1] * a[2];
第五步：b[4] = b[3] * a[3] = a[0] * a[1] * a[2] * a[3];

第二步：计算右上三角，也就是每行【】之后的乘积

第一步
temp *= a[4] = a[4];
b[3] = b[3] * temp = a[0] * a[1] * a[2] * a[4];
第二步
temp *= a[3] = a[4] * a[3];
b[2] = b[2] * temp = a[0] * a[1] * a[4] * a[3];
第三步
temp *= a[2] = a[4] * a[3] * a[2];
b[1] = b[1] * temp = a[0] * a[4] * a[3] * a[2];
第四步
temp *= a[1] = a[4] * a[3] * a[2] * a[1];
b[0] = b[0] * temp = a[4] * a[3] * a[2] * a[1];