#  Merge k Sorted Lists

## 问题分析

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

## 代码实现

1.
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        while len(lists)!=1:
            ceil = len(lists) // 2 + len(lists)%2
            counter = 0
            for i in range(0, len(lists),2):
                if i!=len(lists)-1:
                    lists[counter] = self.mergeTwoLists(lists[i],lists[i+1])
                    counter += 1
            if len(lists)%2 == 1:
                lists[counter]=lists[i]
            lists = lists[:ceil]
        return lists[0]

    def mergeTwoLists(self, l1:ListNode, l2:ListNode)-> ListNode:
        def recursive(ln1,ln2):
            if not ln1: return ln2
            if not ln2: return ln1
            if ln1.val<ln2.val:
                ln1.next = recursive(ln1.next,ln2)
                return ln1
            else:
                ln2.next = recursive(ln1,ln2.next)
                return ln2
        return recursive(l1,l2)
```

2.堆法
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq as hp
        cache = []
        for idx, l in enumerate(lists):
            if l:
                hp.heappush(cache, (l.val,idx))
        dumb = move = ListNode(10086)
        while cache:
            _,idx = hp.heappop(cache)
            cur = lists[idx]
            move.next = cur
            move, cur = move.next, cur.next
            if cur:
                hp.heappush(cache,(cur.val,idx))
                lists[idx] = lists[idx].next
        return dumb.next
```


## 思路总结

方法一复用21.题代码。

方法二堆法，导入heapq包。