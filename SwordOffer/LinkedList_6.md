# 合并两个排序的链表


## 题目描述

输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。


## 代码实现

1. 双指针法
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        new = pHead1 if pHead1.val < pHead2.val else pHead2
        tmp1 = pHead1
        tmp2 = pHead2
        if new == pHead1:
            tmp1 = tmp1.next
        else:
            tmp2 = tmp2.next
        pre = new
        while tmp1 and tmp2:
            if tmp1.val < tmp2.val:
                pre.next = tmp1
                pre = tmp1
                tmp1 = tmp1.next
            else:
                pre.next = tmp2
                pre = tmp2
                tmp2 = tmp2.next
        if tmp1 == None:
            pre.next = tmp2
        else:
            pre.next = tmp1
        return new
```
运行时间：43ms

占用内存：8684k



## 思路总结

首先考虑特殊情况，有一个为空时，返回另一个链表。
然后新链表结点new是两个链表第一个结点中数值较小的结点。
依次遍历所有结点，选择较小的值追加到新链表的结点。
最后返回新链表的头结点new。


