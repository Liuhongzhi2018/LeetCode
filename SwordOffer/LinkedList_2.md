# 链表中环的入口结点


## 题目描述

给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。


## 代码实现

1. 遍历查询
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        applist = []
        point = pHead
        while point:
            if point in applist:
                return point
            else:
                applist.append(point)
            point = point.next
```
运行时间：25ms

占用内存：5856k


2. 快慢指针法
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None or pHead.next == None or pHead.next.next == None:
            return None
        pfast = pHead.next.next
        pslow = pHead.next
        while pfast != pslow:
            if pfast.next == None or pfast.next.next == None:
                return None
            pfast = pfast.next.next
            pslow = pslow.next
        pfast = pHead #让快指针回到头节点
        while pfast != pslow:
            pfast = pfast.next
            pslow = pslow.next
        return pfast
```
运行时间：34ms

占用内存：8220k



## 思路总结

1. 遍历查询法

用列表保存出现过的指针，若指向的结点已出现过则返回该结点。

2. 双指针法

两个指针一个fast、一个slow同时从一个链表的头部出发；fast一次走2步，slow一次走一步，如果该链表有环，两个指针必然在环内相遇；此时只需要把其中的一个指针重新指向链表头部，另一个不变(还在环内),这次两个指针一次走一步，相遇的地方就是入口节点。