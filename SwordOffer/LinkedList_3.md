# 删除链表中重复的结点


## 题目描述

在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5


## 代码实现

1. 遍历查询
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        head = ListNode(-1)
        p = head
        p.next = pHead
        cur = pHead
        while cur and cur.next:
            if cur.val != cur.next.val:
                p = p.next
                cur = cur.next
            else:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                p.next = cur
        return head.next
```
运行时间：23ms

占用内存：5752k




## 思路总结

1. 三指针法

因为重复的节点都要删除，因此需要标记重复开始前的上一个节点，又因为头结点有可能是重复的节点，为了操作方便，我们可以再链表前面设置一个空节点作为头结点，因此需要设置3个指针，第一个head指向头结点。第二个p用来标记重复节点的前面一个节点，第三个cur用来寻找重复的节点，一旦找到p就不移动了，cur继续往后寻找直到不是重复的节点。
