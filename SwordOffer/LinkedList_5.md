# 反转链表


## 题目描述

输入一个链表，反转链表后，输出新链表的表头。


## 代码实现

1. 双指针法
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
        if pHead.next == None:
            return pHead
        fore = pHead
        cur = pHead.next
        rear = cur.next
        fore.next = None
        while rear != None:
            cur.next = fore
            fore = cur
            cur = rear
            rear = rear.next
        cur.next = fore
        return cur
```
运行时间：25ms

占用内存：5988k



## 思路总结

将现有头换成尾，尾部next为空；将从第二个结点开始，指向前一个结点。
需要有一个指针，一直指向还未翻转的结点的头部。


