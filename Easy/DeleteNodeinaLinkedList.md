#  Delete Node in a Linked List

## 问题分析
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

请编写一个函数，使其可以删除某个链表中给定的（非末尾的）节点，您将只被给予要求被删除的节点。

## 代码实现
``` C
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void deleteNode(struct ListNode* node) {
    struct ListNode* next=node->next;
    *node = *next;
    free(next);
}
```

## 总结体会

本题要求在给定链表中删除指定节点，主要考察链表的基本操作。

在函数算法设计上，首先需要明确参数列表中node结构体指针是且必须是链表节点，其次将节点的next指针指向节点赋给node，最后返回node节点即可将指定节点删除。函数最后释放next内存空间。