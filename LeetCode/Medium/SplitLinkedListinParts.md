#  Split Linked List in Parts

## 问题描述

Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.
Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ] 

给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。

每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。

这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。

返回一个符合上述规则的链表的列表。

举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]


## 代码实现

1.
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        cur = root
        for N in range(1001):
            if not cur:
                break
            cur = cur.next
        width, remainder = divmod(N,k)

        ans = []
        cur = root
        for i in range(k):
            head = cur
            for j in range(width + (i < remainder)-1):
                if cur: 
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans
```


## 思路总结

知道每个部分的大小。我们将不创建新列表，而是直接拆分原链表，并根据需要返回指向原始链表中节点的指针列表。