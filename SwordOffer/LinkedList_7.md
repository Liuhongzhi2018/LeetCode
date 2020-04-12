# 复杂链表的复制


## 题目描述


输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）


## 代码实现

1. 内置深拷贝函数
```python
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
import copy

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        newlink = copy.deepcopy(pHead)
        return newlink
```
运行时间：31ms

占用内存：6008k

2.复制结点
```python
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return None
        cur = pHead
        while cur:
            node = RandomListNode(cur.label)
            node.next = cur.next
            cur.next = node
            cur = node.next

        cur = pHead
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
            
        cur = pHead
        newHead = pHead.next
        pnew = pHead.next
        while cur:
            cur.next = cur.next.next
            if pnew.next:
                pnew.next = pnew.next.next
                pnew = pnew.next
            cur = cur.next
        return newHead
```
运行时间：30ms

占用内存：6340k



## 思路总结

1. 区分深拷贝和浅拷贝的区别。

2. 复制一个一样的node，添加到之前链表的每一个node后面，并且移动cur指针。A.next = A'
实现新建node的random指向。A.next.random = A.random.next
断开原来node和新node之间的链接。