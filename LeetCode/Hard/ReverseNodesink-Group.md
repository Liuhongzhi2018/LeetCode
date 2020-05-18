#  Reverse Nodes in k-Group

## 问题分析

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。



## 代码实现

1.
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dumb = ListNode(10086)
        dumb.next = head
        end = prev = dumb
        def swap(prev,k,end):
            after = end.next
            move = prev.next
            prev.next = end
            temp = move.next
            end = move
            for i in range(k-1):
                tnext = temp.next
                temp.next = move
                move = temp
                temp = tnext
            end.next = after
            return end

        while True:
            try:
                for _ in range(k):
                    end = end.next
                prev = end = swap(prev, k, end)
            except:
                break
        return dumb.next
```

2.
```python


```

## 思路总结

这题是24题的扩展题。  

1. 提取要翻转的元素；  
2. 改变指针；  
3. 移动move和temp；

首先定义一个假头部减少if-else语句，然后声明swap function 执行翻转k个链表指针的操作，执行次数通过try-except执行报错后退出。