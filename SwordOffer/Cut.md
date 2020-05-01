#  剪绳子


## 题目描述






## 代码实现

1. 动态规划
```python
# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        n = number
        if n<2:
            return 0
        if n==2:
            return 1
        if n==3:
            return 2
        l=[0,1,2,3] 
        #l中存放着长度为i的绳子剪成若干段长度的最大乘积，i从0开始
        for i in range(4,n+1):
            max=0
            for j in range(1,i//2+1):
                temp=l[j]*l[i-j]
                if temp>max:
                    max=temp
            l.append(max)
        return l[n]
```
运行时间：27ms

占用内存：5740k


2. 
```python
# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        n = number
        if n<2:
            return 0
        if n==2:
            return 1
        if n==3:
            return 2
        multi_3=0
        while n>4:
            multi_3+=1
            n-=3
        return 3**multi_3*n
```
运行时间：28ms

占用内存：5860k



## 思路总结

1. 动态规划  
动态规划，先自上而下分析，在长度为n的绳子所求为f(n)，剪下一刀后剩下的两段长度是i和n-i，在这个上面还可能继续减(子问题)  
然后自下而上的解决问题，可以从f(1)开始向上计算并保存，最终获得f(n)的值。
由于当i大于n//2时，就不用在计算了

2. 贪婪算法  
当n>=5的时候，尽可能多的剪长度为3的绳子，将长度为n的绳子一值减到长度为4的时候，停止。