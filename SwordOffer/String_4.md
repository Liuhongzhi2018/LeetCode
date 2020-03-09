# 字符流中第一个不重复的字符


## 题目描述

请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。


## 代码实现

1. 哈希查找法
```python
# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.list_ch = []
        self.dict_all = {}
    def FirstAppearingOnce(self):
        # write code here
        if self.dict_all is None:
            return '#'
        for i in self.list_ch:
            if self.dict_all[i] == 1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.list_ch.append(char)
        if char not in self.dict_all:
            self.dict_all[char] = 1
        else:
            self.dict_all[char] += 1
```
运行时间：32ms

占用内存：5704k


2. 字符计数法
```python
# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self): 
        self.str='' 
        self.count=[0 for _ in range(256)]
    def FirstAppearingOnce(self): 
        # write code here 
        for i in self.str: 
            if self.count[ord(i)]==1: 
                return i 
        return '#' 
    def Insert(self, char): 
        # write code here 
        self.str+=char 
        self.count[ord(char)]+=1
```
运行时间：30ms

占用内存：5728k



## 思路总结

1. 哈希查找法。用字典的键对应字符，值对应出现的次数。

2. 字符计数法。将出现的字符对应到10进制位置，用count统计出现的次数。