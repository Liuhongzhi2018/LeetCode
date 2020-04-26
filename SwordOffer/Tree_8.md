# 数据流中的中位数


## 题目描述

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

## 代码实现

1. 最大堆和最小堆
```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.littleValueMaxHeap = [] 
        self.bigValueLittleHeap = [] 
        self.maxcount = 0 
        self.littlecount = 0
        
    def Insert(self, num):
        # write code here
        if self.maxcount > self.littlecount:
            self.littlecount += 1 
            if num < self.littleValueMaxHeap[0]: 
                tempNum = self.littleValueMaxHeap[0]
                self.adjustmaxHeap(num)
                self.creatlittleHeap(tempNum) 
            else: self.creatlittleHeap(num) 
        else: 
            self.maxcount += 1
            if len(self.littleValueMaxHeap) == 0: 
                self.creatmaxHeap(num) 
            else: 
                if self.bigValueLittleHeap[0] < num:
                    tempNum = self.bigValueLittleHeap[0] 
                    self.adjustlittleHeap(num)
                    self.creatmaxHeap(tempNum) 
                else: 
                    self.creatmaxHeap(num)
    def GetMedian(self,n=None):
        # write code here
        if self.littlecount < self.maxcount: 
            return self.littleValueMaxHeap[0] 
        else: 
            return float(self.littleValueMaxHeap[0] + self.bigValueLittleHeap[0]) / 2 
        
    def creatmaxHeap(self, num): 
        self.littleValueMaxHeap.append(num) 
        tempIndex = len(self.littleValueMaxHeap) - 1 
        while tempIndex: 
            parentIndex = (tempIndex - 1) // 2 
            if self.littleValueMaxHeap[parentIndex] < self.littleValueMaxHeap[tempIndex]: 
                self.littleValueMaxHeap[parentIndex], self.littleValueMaxHeap[tempIndex] \
                = self.littleValueMaxHeap[tempIndex],self.littleValueMaxHeap[parentIndex]
                tempIndex=parentIndex 
            else: 
                break
        
    def adjustmaxHeap(self, num):
        if num < self.littleValueMaxHeap[0]: 
            maxHeapLen = len(self.littleValueMaxHeap) 
            self.littleValueMaxHeap[0] = num 
            tempIndex = 0 
            while tempIndex < maxHeapLen: 
                leftIndex = tempIndex * 2 + 1 
                rightIndex = tempIndex * 2 + 2 
                largeIndex = 0 
                if rightIndex < maxHeapLen: 
                    largeIndex = rightIndex \
                    if self.littleValueMaxHeap[leftIndex] < self.littleValueMaxHeap[rightIndex] else leftIndex 
                elif leftIndex < maxHeapLen: 
                    largeIndex = leftIndex 
                else: 
                    break 
                if self.littleValueMaxHeap[tempIndex] < self.littleValueMaxHeap[largeIndex]:
                    self.littleValueMaxHeap[tempIndex], self.littleValueMaxHeap[largeIndex] \
                    = self.littleValueMaxHeap[ largeIndex],self.littleValueMaxHeap[tempIndex] 
                    tempIndex = largeIndex 
                else: 
                    break
        
    def creatlittleHeap(self, num):
        self.bigValueLittleHeap.append(num)
        tempIndex = len(self.bigValueLittleHeap) - 1 
        while tempIndex:
            parentIndex = (tempIndex - 1) // 2 
            if self.bigValueLittleHeap[tempIndex] < self.bigValueLittleHeap[parentIndex]: 
                self.bigValueLittleHeap[parentIndex], self.bigValueLittleHeap[tempIndex] \
                = self.bigValueLittleHeap[ tempIndex], self.bigValueLittleHeap[ parentIndex] 
                tempIndex = parentIndex 
            else:
                break
                
    def adjustlittleHeap(self, num):
        if num < self.bigValueLittleHeap[0]: 
            maxHeapLen = len(self.bigValueLittleHeap) 
            self.bigValueLittleHeap[0] = num 
            tempIndex = 0
            while tempIndex < maxHeapLen:
                leftIndex = tempIndex * 2 + 1 
                rightIndex = tempIndex * 2 + 2 
                largeIndex = 0 
                if rightIndex < maxHeapLen: 
                    largeIndex = rightIndex \
                    if self.bigValueLittleHeap[rightIndex] < self.bigValueLittleHeap[ leftIndex] else leftIndex 
                elif leftIndex < maxHeapLen: 
                    largeIndex = leftIndex 
                else: 
                    break 
                if self.bigValueLittleHeap[largeIndex] < self.bigValueLittleHeap[tempIndex]: 
                    self.bigValueLittleHeap[tempIndex], self.bigValueLittleHeap[largeIndex] \
                    = self.bigValueLittleHeap[ largeIndex], self.bigValueLittleHeap[tempIndex] 
                    tempIndex = largeIndex
                else: 
                    break
```
运行时间：21ms

占用内存：5728k



## 思路总结

插入元素时，先插入最大堆，与堆顶判断，如果大的话，将最大堆的堆顶移到最小堆的堆顶。  
如果是奇数个数，取最大堆的堆顶；如果是偶数，取最大和最小堆。  

相似功能的函数进行封装。