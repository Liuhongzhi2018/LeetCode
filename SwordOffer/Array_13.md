# 数组中的逆序对


## 题目描述

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

## 代码实现

1. 归并思想
```python
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        global count 
        count=0 
        
        def A(array): 
            global count 
            if len(array)<=1: 
                return array 
            k=int(len(array)/2) 
            left=A(array[:k]) 
            right=A(array[k:]) 
            l,r = 0,0 
            result=[] 
            while l<len(left) and r<len(right): 
                if left[l]<right[r]: 
                    result.append(left[l]) 
                    l+=1 
                else: 
                    result.append(right[r]) 
                    r+=1 
                    count+=len(left)-l 
                    
            result+=left[l:] 
            result+=right[r:] 
            return result
        A(data)
        return count%1000000007
```
运行时间：3156ms

占用内存：23108k



## 思路总结

1. 根绝归并排序的原理，可得到时间复杂度为O(n * logn)的方法，也就是在归并排序法的基础上添加一行代码：cout=+len(left)-l
