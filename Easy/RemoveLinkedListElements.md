#  Remove Linked List Elements

## 问题分析
Remove all elements from a linked list of integers that have value val.

删除链表中等于给定值 val 的所有节点。


## 代码实现
``` C
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    if (head == NULL) return NULL;
    struct ListNode* point =head;
    while(point->next!=NULL){
        if(point->next->val==val) point->next=point->next->next;
        else point=point->next;
    }
    return head->val==val?head->next:head;
}
```

## 总结体会

本题要求删除链表中节点值等于给定值的节点，主要考察链表节点的遍历和删除操作。

在算法设计上，首先判断节点是否为空；其次遍历链表节点，如果节点值等于给定值，则通过next指针变量，删除该节点，直至删除所有符合要求节点。

第一次编译时是return head，OJ时报错，没有考虑到链表只有一个节点[1]且给定值为1，修改为return head->val==val?head->next:head的判断条件，OJ Accepted。