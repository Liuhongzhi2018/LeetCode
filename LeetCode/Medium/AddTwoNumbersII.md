#  Add Two Numbers II

## 问题描述

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed. 

给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。


## 代码实现

1.
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1

        def link2num(node):
            res = 0
            while node:
                res = res * 10 + node.val
                node = node.next
            return res

        ret = link2num(l1) + link2num(l2)
        dummy = ListNode(0)
        p = dummy
        for i in str(ret):
            dummy.next = ListNode(int(i))
            dummy = dummy.next
        return p.next
```


## 思路总结

首先将链表转换为数字(int)；  
然后创建虚拟哑结点dummynode；  
在for循环里将结果相加结果转换为字符，然后逐位取出；  
将取出的字符逐位放入新建的链表。