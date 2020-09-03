#  Palindrome Linked List

## 问题分析

Given a singly linked list, determine if it is a palindrome.

请判断一个链表是否为回文链表。


## 代码实现

1.
``` C
struct ListNode* temp;
bool list(struct ListNode* p);
bool isPalindrome(struct ListNode* head);

bool list(struct ListNode* p) {
    if (p == NULL) return true;
    bool isPal = list(p->next)&(temp->val == p->val);
    temp = temp->next;
    return isPal;
}
bool isPalindrome(struct ListNode* head) {
    temp = head;
    return list(head);
}
```

2.将值复制到数组中后用双指针法
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        cur = head
        while cur is not None:
            vals.append(cur.val)
            cur = cur.next
        return vals == vals[::-1]
```

## 总结体会

本题要求判断给定链表是否为回文链表。

算法设计上定义temp结构体指针为全局变量，用isPalindrome返回是否为符合条件的链表，用list函数进行判断。首先判断链表是否为空，如果链表为空判断是回文链表，返回true。然后用list函数进行回文链表的判断，当isPal返回true时，则链表为满足条件链表。

需要注意的是，bool list(struct ListNode* p)要求先声明再使用，否则会报出conflicting types for list错误。

有两种常用的列表实现，一种是数组列表和链表。如果我们想在列表中存储值，那么它们是如何保存的呢？

    数组列表底层是使用数组存储值，我们可以通过索引在 O(1)O(1)O(1) 的时间访问列表任何位置的值，这是由于内存寻址的方式。
    链表存储的是称为节点的对象，每个节点保存一个值和指向下一个节点的指针。访问某个特定索引的节点需要 O(n)O(n)O(n) 的时间，因为要通过指针获取到下一个位置的节点。