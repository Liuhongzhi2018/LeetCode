# 两个链表的第一个公共结点


## 题目描述


输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）


## 代码实现

1. 快慢指针
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        cur1 = pHead1
        cur2 = pHead2
        while cur1 and cur2:
            if cur1 == cur2:
                return cur1
            cur1 = cur1.next
            cur2 = cur2.next
        if cur1:
            return self.equal(cur2,cur1,pHead2,pHead1)
        else:
            return self.equal(cur1,cur2,pHead1,pHead2)
        '''
        k = 0
        if cur1:
            while cur1:
                cur1 = cur1.next
                k += 1
            cur1 = pHead1
            cur2 = pHead2
            for i in range(k):
                cur1 = cur1.next
                
            while cur1 != cur2:
                cur1 = cur1.next
                cur2 = cur2.next
            return cur1
        else:
            while cur2:
                cur2 = cur2.next
                k += 1
            cur1 = pHead1
            cur2 = pHead2
            for i in range(k):
                cur2 = cur2.next
                
            while cur1 != cur2:
                cur1 = cur1.next
                cur2 = cur2.next
            return cur1
        '''
    def equal(self,shortP,longP,shortH,longH):
            k = 0
            while longP:
                longP = longP.next
                k += 1
            cur1 = shortH
            cur2 = longH
            for i in range(k):
                cur2 = cur2.next
                
            while cur1 != cur2:
                cur1 = cur1.next
                cur2 = cur2.next
            return cur1
```
运行时间：31ms

占用内存：5740k





## 思路总结

先找出链表长度之间的差值。
然后让长的链表先走差值的步数。
注意，当两个链表一样长时，通过比较返回结点。