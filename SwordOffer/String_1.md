# 替换空格


## 题目描述

请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。


## 代码实现

1. 查找并替换
```python
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        new = ""
        for i in s:
            if i == ' ':
                new += "%" + str(20)
            else:
                new += i
                # print(i)
        return new
```
运行时间：25ms

占用内存：5984k

2. 字符串转列表遍历
```python
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = list(s) 
        l = len(s) 
        for i in range(l): 
            if s[i]==' ': 
                s[i]='%20' 
        return ''.join(s)
```
运行时间：25ms

占用内存：5988k

3. 内置函数
```python
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ','%20')
```
运行时间：22ms

占用内存：5628k




## 思路总结

1. 查找替换。遍历字符串的元素，如果遇到空格则替换，然后继续追加字符串。

2. 将字符串转成list，然后按照下标顺序遍历列表元素。