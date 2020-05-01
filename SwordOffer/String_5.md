# 第一个只出现一次的字符


## 题目描述

在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）


## 代码实现

1. 遍历法
```python
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s=='':
            return -1
        if len(s)==1:
            return 0
        char_list=[]
        index_list=[]
        flag_list=[]
        for i,c in enumerate(s):
            if c not in char_list:
                char_list.append(c)
                index_list.append(i)
                flag_list.append(True)
            else:
                position=char_list.index(c)
                flag_list[position]=False
        # print(char_list,index_list,flag_list)
        for pos,flag in enumerate(flag_list):
            if flag:
                return index_list[pos]
        return -1
```
运行时间：30ms

占用内存：5860k

2. 哈希表
```python
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s=='':
            return -1
        if len(s)==1:
            return 0
        hash_table=[0]*256
        for c in s:
            hash_table[ord(c)]+=1
        for i,c in enumerate(s):
            if hash_table[ord(c)]==1:
                return i
        return -1
```
运行时间：28ms

占用内存：5860k


## 思路总结

1. 不能用python中的字典结构来实现，因为字典中的键是无序排列的  
对原来的长字符串进行遍历和索引，填充如下三个列表中的数值：  
char_list    长度为原始字符串中一共出现了多少个不同的字符，每个元素为不重复的字符  
index_list   char_list中的每个字符串出现在原始字符串中的第一个位置索引  
flag_list    表示char_list中的字符是否在原始长字符串中只出现一次  
三个列表长度相等  

2. 为当前输入的长字符串构建哈希表，哈希表以列表形式/顺序表存储
由于会出现所有的大写字母和所有的小写字母,故而哈希表的长度为256
字符长度为8的数据类型,共有256种可能,于是创建一个长度为256的列表
因为a的ASCII码值为65，   z的ASCII码值为122
构建好哈希表之后，由于哈希表是顺序存储的，所以仍然不知道在原字符串中出现的第一个字符是什么
故而需要对原字符串进行再次遍历