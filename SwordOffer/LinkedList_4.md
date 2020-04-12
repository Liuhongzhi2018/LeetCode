# 链表中倒数第k个结点


## 题目描述

输入一个链表，输出该链表中倒数第k个结点。


## 代码实现

1. 双指针法
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        foreP = head
        rear = head
        for i in range(k):
            if rear == None:
                return None
            rear = rear.next
        while rear:
            rear = rear.next
            foreP = foreP.next
            
        return foreP
```
运行时间：25ms

占用内存：5852k



## 思路总结

边界条件，K如果比链表长度大，结果返回None。注意需要先判断，再移动标尺范围，不能遇到两次None。
K如果小于链表长度，定义两个前后指针，中间间隔是k，当后指针到链表尾部时，前指针为所有结点。


