# 最小的K个数


## 题目描述

输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

## 代码实现

1. 内置sort函数和切片
```python
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput==[]:
            return []
        if k>len(tinput):
            return []
        tinput.sort()
        return tinput[:k]
```
运行时间：29ms

占用内存：5712k


2.最大堆
```python
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        
        #创建最大堆或者是插入最大堆
        def createMaxHeap(num):
            maxHeap.append(num)
            currentIndex=len(maxHeap)-1
            while currentIndex != 0:
                parentIndex=(currentIndex-1)>>1#相当于parentIndex=(currentIndex-1)//2，目的是为了寻找父结点
                if maxHeap[parentIndex]<maxHeap[currentIndex]:#和父结点进行比较
                    maxHeap[parentIndex],maxHeap[currentIndex]=maxHeap[currentIndex],maxHeap[parentIndex]
                else:
                    break
        
        #当根结点变化时，如何调整最大堆 
        def adjustMaxHeap(num):
            if num<maxHeap[0]: 
                maxHeap[0]=num 
            maxHeapLen=len(maxHeap)
            index=0 
            while index<maxHeapLen:
                leftIndex=index*2+1
                rightIndex=index*2+2
                largerIndex=0
                if rightIndex<maxHeapLen: 
                    if maxHeap[rightIndex]<maxHeap[leftIndex]:
                        largerIndex=leftIndex 
                    else: largerIndex=rightIndex 
                # 没有right
                elif leftIndex<maxHeapLen:
                    largerIndex=leftIndex 
                # 既没有left也没有right
                else: 
                    break 
                # 替换
                if maxHeap[index]<maxHeap[largerIndex]:
                    maxHeap[index],maxHeap[largerIndex]=maxHeap[largerIndex],maxHeap[index] 
                index=largerIndex 
                
        maxHeap=[]
        inputLen=len(tinput) 
        if inputLen<k or k<=0: 
            return [] 
        for i in range(inputLen):
            if i<k:
                createMaxHeap(tinput[i]) 
            else: 
                adjustMaxHeap(tinput[i])
        maxHeap.sort()   # 没有返回值
        return maxHeap
```
运行时间：24ms

占用内存：5720k

## 思路总结

小值大堆，大值小堆。

最大堆：  
最大堆是堆的两种形式之一。  
根结点（亦称为堆顶）的关键字是堆里所有结点关键字中最大者，称为大根堆，又称最大堆（大顶堆）。  
大根堆要求根节点的关键字既大于或等于左子树的关键字值，又大于或等于右子树的关键字值。  
时间复杂度O(logn)  
替换复杂度O(logn)

插入过程和调整结点过程。

最小堆：  
是一种经过排序的完全二叉树，其中任一非终端节点的数据值均不大于其左子节点和右子节点的值。

注意：比较时最好用小于号，用到库时，可能小的优先级高。
