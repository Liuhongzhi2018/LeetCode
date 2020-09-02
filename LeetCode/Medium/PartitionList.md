#  Partition List

## 问题描述

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。


## 代码实现

1.
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            
            head = head.next
        
        after.next = None
        before.next = after_head.next

        return before_head.next
```


## 思路总结

对该问题的逆向工程告诉我们，如果我们在特定值 JOINT将改后链表拆分，我们会得到两个更小的链表，其中一个包括全部值小于x的元素，另一个包括全部值大于x的元素。在解法中，我们的主要目的是创建这两个链表，并将它们连接。

算法：  
初始化两个指针 before 和 after。在实现中，我们将两个指针初始化为哑 ListNode。这有助于减少条件判断。   
利用head指针遍历原链表。  
若head 指针指向的元素值 小于 x，该节点应当是 before 链表的一部分。因此我们将其移到 before 中。  
否则，该节点应当是after 链表的一部分。因此我们将其移到 after 中。  
遍历完原有链表的全部元素之后，我们得到了两个链表 before 和 after。原有链表的元素或者在before 中或者在 after 中，这取决于它们的值。  
现在，可以将 before 和 after 连接，组成所求的链表。  
为了算法实现更容易，我们使用了哑结点初始化。不能让哑结点成为返回链表中的一部分，因此在组合两个链表时需要向前移动一个节点。
