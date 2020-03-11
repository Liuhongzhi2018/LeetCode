# 从尾到头打印链表


## 题目描述

输入一个链表，按链表从尾到头的顺序返回一个ArrayList。


## 代码实现

1. 递归法
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode: 
            return [] 
        res = self.printListFromTailToHead(listNode.next) 
        res.append(listNode.val) 
        return res
```
运行时间：23ms

占用内存：5856k

2. 顺序遍历反向输出
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        adver = []
        while listNode:
            adver.append(listNode.val)
            listNode = listNode.next
        return adver[::-1]
```
运行时间：24ms

占用内存：5860k


## 思路总结

1. 递归法

n次找到最后的链表节点，n次返回。

2. 顺序遍历反向输出

从头到尾遍历链表，将值存在列表adver中，最后将adver逆序输出。