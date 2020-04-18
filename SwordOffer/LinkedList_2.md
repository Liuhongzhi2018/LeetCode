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


```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None:
            return None
        fastp = pHead
        slowp = pHead 
        while fastp and fastp.next:
            fastp = fastp.next.next
            slowp = slowp.next
            if fastp == slowp:
                break
        if fastp == None or fastp.next == None:
            return None
        fastp = pHead
        while fastp != slowp:
            fastp = fastp.next
            slowp = slowp.next
        return fastp
```
运行时间：25ms

占用内存：5860k


## 思路总结

1. 遍历查询法

用列表保存出现过的指针，若指向的结点已出现过则返回该结点。

2. 双指针法

两个指针一个fast、一个slow同时从一个链表的头部出发；fast一次走2步，slow一次走一步，如果该链表有环，两个指针必然在环内相遇；此时只需要把其中的一个指针重新指向链表头部，另一个不变(还在环内),这次两个指针一次走一步，相遇的地方就是入口节点。

如果slowp走了L长度，fastp走了2L长度。假设从开始到入口的长度是s，slowp在环内的长度是d，那么L = s + d。假设环内slow未走的长度是m，fastp走的长度是s + n × (m+d) + d = 2L = 2 (s + d)，则开始到入口的长度 s = m + (n-1) × d。可以理解为相遇时，slowp继续走到环起点，与fastp从开始到环起点，距离相同。 