#  丑数


## 题目描述

把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。



## 代码实现

1. 后丑数由前丑数得到
```python
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        i = 1
        t2 = m2 = 0
        t3 = m3 = 0
        t5 = m5 = 0
        n = index
        uglynum = [1]
        while i < n:
            for x in range(t2, len(uglynum)):
                m2 = uglynum[x]*2
                if m2 > uglynum[-1]:
                    t2 = x
                    break
            for x in range(t3, len(uglynum)):
                m3 = uglynum[x]*3
                if m3 > uglynum[-1]:
                    t3 = x
                    break
            for x in range(t5, len(uglynum)):
                m5 = uglynum[x]*5
                if m5 > uglynum[-1]:
                    t5 = x
                    break
            uglynum.append(min(m2,m3,m5))
            i += 1
        return uglynum[-1]
```
运行时间：38ms

占用内存：5708k


```python
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        ugly = [1]
        two = 0
        three = 0
        five = 0
        count = 1
        while count != index:
            minValue = min(2*ugly[two],3*ugly[three],5*ugly[five])
            ugly.append(minValue)
            count += 1
            if minValue == 2*ugly[two]:
                two += 1
            if minValue == 3*ugly[three]:
                three += 1
            if minValue == 5*ugly[five]:
                five += 1
        return ugly[count-1]
```
运行时间：23ms

占用内存：5852k


## 思路总结

循环找丑数。  
判断一个数是不是丑数，先循环除以2，直到不能整除；循环除以3，直到不能整除；循环除以5，直到不能整除。
这时如果剩余值是1，就可以认为是丑数。  
其他情况不是丑数。

现有的最大丑数M来生成下一个丑数，该丑数肯定是前面某一个丑数乘以2、3或者5的结果。  
首先考虑把已有的每个丑数乘以2。在乘以2的时候，能得到若干个结果小于或等于M的。  
由于是按照顺序生成的，小于或者等于M肯定已经在数组中了，不需再次考虑；还会得到若干个大于M的结果，但只需要第一个大于M的结果，因为我们希望丑数是按从小到大顺序生成的，其他更大的结果我们以后再说。  
把得到的第一个乘以2后大于M的结果，记为M2。同样我们把已有的每一个丑数乘以3和5，能得到第一个大于M的结果M3和M5。那么下一个丑数应该是M2、M3和M5三个数的最小者。