#  Intersection of Two Linked Lists

## 问题分析
Write a program to find the node at which the intersection of two singly linked lists begins.

Notes:

* If the two linked lists have no intersection at all, return null.
* The linked lists must retain their original structure after the function returns.
* You may assume there are no cycles anywhere in the entire linked structure.
* Your code should preferably run in O(n) time and use only O(1) memory.

编写一个程序，找到两个单链表相交的起始节点。

注意：

* 如果两个链表没有交点，返回 null。
* 在返回结果后，两个链表仍须保持原有的结构。
* 可假定整个链表结构中没有循环。
* 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

## 代码实现
``` C
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode *p1 = headA;
    struct ListNode *p2 = headB;
    if (p1 == NULL || p2 == NULL) return NULL;
    while ((p1!=NULL)&&(p2!= NULL)&&(p1!=p2))
    {
        p1 = p1->next;
        p2 = p2->next;
        if (p1 == p2) return p1;
        if (p1 == NULL) p1 = headB;
        if (p2 == NULL) p2 = headA;
    }
    return p1;
}  
```

## 总结体会

本题要求两链表的相交的起点，即从相交点后的链表结点相同。

首先需要判断有几种情况：第1种，两链表为空链表；第2种，两条不相交链表；第3种，两条相交的链表。

其次，开始编程时，将空链表情况放在循环开始前进行讨论，均为空则返回；进入循环的条件是，两链表均不为空且头结点不相交时，进入循环，如果第一个结点就相交则返回任意结点，本题代码返回P1；循环中双指针遍历时，如果p1==p2，则跳出循环，返回第一个相交结点。











