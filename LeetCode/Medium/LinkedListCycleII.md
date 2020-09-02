#  Linked List Cycle II

## 问题描述

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。


## 代码实现

1.
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set() 
        node = head 
        
        while node is not None: 
            if node in visited: 
                return node 
            
            else: 
                visited.add(node) 
                node = node.next 
        return None
```


## 思路总结

如果我们用一个 Set 保存已经访问过的节点，我们可以遍历整个列表并返回第一个出现重复的节点。

首先，我们分配一个 Set 去保存所有的列表节点。我们逐一遍历列表，检查当前节点是否出现过，如果节点已经出现过，那么一定形成了环且它是环的入口。否则如果有其他点是环的入口，我们应该先访问到其他节点而不是这个节点。其他情况，没有成环则直接返回 null 。

算法会在遍历有限个节点后终止，这是因为输入列表会被分成两类：成环的和不成环的。一个不成环的列表在遍历完所有节点后会到达 null - 即链表的最后一个元素后停止。一个成环列表可以想象成是一个不成环列表将最后一个 null 元素换成环的入口。

如果 while 循环终止，我们返回 null 因为我们已经将所有的节点遍历了一遍且没有遇到重复的节点，这种情况下，列表是不成环的。对于循环列表， while 循环永远不会停止，但在某个节点上， if 条件会被满足并导致函数的退出。