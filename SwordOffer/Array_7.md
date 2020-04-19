# 数组中只出现一次的数字


## 题目描述

一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。


## 代码实现

1. 字典存储元素
```python
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        numsCount = {}
        numLen = len(array)
        ret = []
        for num in array:
            if num in numsCount:
                numsCount[num] += 1
            else:
                numsCount[num] = 1
        for num in numsCount:
            if numsCount[num] == 1:
                ret.append(num)
        if ret != []:
            return ret
        return 0
```
运行时间：26ms

占用内存：5712k


2.位运算
```python
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if len(array) < 2:
            return None
        twoNumXor = None
        for num in array:
            if twoNumXor == None:
                twoNumXor = num
            else:
                twoNumXor = twoNumXor ^ num
                 
        count = 0
        while twoNumXor  % 2 == 0:
            twoNumXor = twoNumXor >> 1
            count += 1
        mask = 1 << count
        
        firstNum = None
        secondNum = None
        for num in array:
            if mask & num == 0:
                if firstNum == None:
                    firstNum = num
                else:
                    firstNum = firstNum ^ num
                    
            else:
                if secondNum == None:
                    secondNum = num
                else:
                    secondNum = secondNum ^ num
        return firstNum,secondNum
```
运行时间：28ms

占用内存：5868k


## 思路总结

1.用字典存储数组每个数字以及出现次数，然后将出现次数为1，即键值为1的数字返回。

2. 位运算
首先位运算中异或的性质：两个相同数字异或=0，一个数和0异或还是它本身。  
当只有一个数出现一次时，我们把数组中所有的数，依次异或运算，最后剩下的就是落单的数，因为成对儿出现的都抵消了。  
依照这个思路，我们来看两个数（我们假设是AB）出现一次的数组。我们首先还是先异或，剩下的数字肯定是A、B异或的结果，这个结果的二进制中的1，表现的是A和B的不同的位。我们就取第一个1所在的位数，假设是第3位，接着把原数组分成两组，分组标准是第3位是否为1。如此**相同的数肯定在一个组**，因为相同数字所有位都相同，而不同的数，肯定不在一组。然后把这两个组按照最开始的思路，依次异或，剩余的两个结果就是这两个只出现一次的数字。