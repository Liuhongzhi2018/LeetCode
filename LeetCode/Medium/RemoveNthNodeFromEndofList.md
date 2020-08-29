# Remove Nth Node From End of List

## 问题分析
Given a linked list, remove the n-th node from the end of list and return its head.

给定一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。


## 代码实现

1.
``` C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int i;
        if (n<1) return head;
        if (!head->next) return NULL;
        ListNode *pre = head, *cur = head;
        for (i = 0; i < n; i++)   cur = cur->next;
        if (!cur) return head->next;
        while (cur->next) {
            cur = cur->next;
            pre = pre->next;
        }
        pre->next = pre->next->next;
        return head;
    }
};
```

2.双指针法
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        dummy = l = r = ListNode(10086)
        dummy.next = head
        for i in range(n):
            r = r.next
        while r.next is not None:
            r = r.next
            l = l.next
        l.next = l.next.next
        return dummy.next
```

3.遍历两遍
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        lenlist = 0
        cur = head
        while cur:
            lenlist += 1
            cur = cur.next
        
        loc = lenlist - n + 1
        cur = head
        p = 1
        if p == loc:
            return head.next
        while p < loc-1:
            p += 1
            cur = cur.next
        cur.next = cur.next.next
        return head
```

## 总结体会

本题要求找到第n个倒数的结点，删除后返回头结点，实际上是对链表结点的遍历，然后返回修改后的链表。

在算法设计上，首先判断要求的结点位置是否在链表中，若不在返回头结点；其次判断倒数n的位置，如果cur为空，则返回头结点，否则返回pre对应的元素即为需要删除的结点；最后返回头指针，即为所求链表。

方法二用两个指针，让r走在l指针前n步；考虑边缘条件，r到走到链表尾部，这时增加一个假头部dummy返回即可。