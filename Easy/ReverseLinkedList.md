#  Reverse Linked List

## 问题分析
Reverse a singly linked list.

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

反转一个单链表。

进阶: 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？


## 代码实现
``` C
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *pre, *cur, *next;
    if (head == NULL ) return NULL;
    if (head->next == NULL) return head;
    pre = head;
    cur = head->next;
    pre->next = NULL;
    while (cur) {
        next = cur->next;
        cur->next = pre;
        pre = cur;
        cur = next;
    }
    return pre;
}
```

## 总结体会

本题要求对单向链表反转，从算法设计上可以采用迭代和递归两种。链表反转操作的顺序对于迭代来说是从链头到链尾。

首先对于链表设置两个指针pre和cur，分别指向表头指针和当前指针。然后依次将旧链表上每一节点添加在新链表的后面，新链表的头指针移向新的链表头。设置一个临时指针next，先暂时指向cur->next指向的地址空间，保存原链表后续数据。然后两两交换改变链表方向，直到所有循环访问完成。当cur指针指向NULL停止迭代，此时链表已完成反转。