#  Linked List Cycle

## 问题分析
Given a linked list, determine if it has a cycle in it.

Follow up: Solve it without using extra space.

给定一个链表，判断链表中是否有环。

进阶：不使用额外空间解决此题。

## 代码实现
``` C
/**
* Definition for singly-linked list.
* struct ListNode {
*     int val;
*     struct ListNode *next;
* };
*/
bool hasCycle(struct ListNode *head) {
    struct ListNode *point = head;
    if (head==NULL)  return false;
    while (head!=NULL) {
        head = head->next;
        if ((point->next != NULL) && (point->next->next != NULL))
            point = point->next->next;
        else  return false;
        if (point == head) return true;
    }
    return false;
}
```

## 总结体会

本题要求判断链表是否有环，若成环时则某一个节点是自身或者自己的祖先，主要有3种情况：空链表不成环，一个节点自成环和一条链表有完整环。在算法设计上，可以将链表元素保存在一个数组中，若题设要求无额外空间，则需要两个指针指向链表元素且步进值差1，存在环的情况时指针必会重合。

因此程序设计上，首先判断是否为空链表，若是则不存在环；其次分别用head和point两个指针，head步进为1，point步进为2，若指针重合为存在环，返回true，否则返回false，完成链表内环的判断。











