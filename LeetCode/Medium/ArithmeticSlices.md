#  Arithmetic Slices

## 问题描述

如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

如果满足以下条件，则称子数组(P, Q)为等差数组：

元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

函数要返回数组 A 中所有为等差数组的子数组个数。



## 代码实现

1.动态规划
```python
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3: 
            return 0 
        d = A[1]-A[0] 
        index = [0] 
        res = 0 
        k = 0 
        
        for i in range(1, len(A)-1): 
            if A[i+1]-A[i] == d:
                k = i+1 
                continue 
            else: 
                d = A[i+1]-A[i] 
                index.append(i) 
                if index[-1]-index[-2]+1 >= 3: 
                    length = index[-1]-index[-2]+1 
                    res += (length-2)*(length-1)//2 
            
        if k == len(A)-1: 
            index.append(k) 
            if index[-1]-index[-2]+1 >= 3: 
                length = index[-1]-index[-2]+1 
                res += (length-2)*(length-1)//2 
        
        return res
```

2.动态规划
```python
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A) 
        if n <3: 
            return 0 
            
        dp = [0]*n 
        array_sum = 0 
        for i in range(2,n): 
            if A[i] - A[i-1] == A[i-1] - A[i-2]: 
                dp[i] = dp[i-1] + 1
                array_sum += dp[i]
        
        return array_sum
```



## 思路总结

A的长度必须超过3，统计出所有的等差数列组合，再利用高斯求和公式计算子组合数即可。