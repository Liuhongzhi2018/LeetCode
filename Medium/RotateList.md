#  Rotate List

## 问题分析
Given a linked list, rotate the list to the right by k places, where k is non-negative.

给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

## 代码实现
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
    ListNode* rotateRight(ListNode* head, int k) {
    if(head==nullptr||k==0)   return head;
        int step,len=1;
        ListNode *p=head;
        while(p->next){
            len++;
            p=p->next;
        }
        k=len-k%len;
        p->next=head;
        for(step=0;step<k;step++){
            p=p->next;
        }
        head=p->next;
        p->next=nullptr;
        return head;
    }
};
```

## 总结体会

本题要求根据给定的旋转链表，向右旋转k步，进行链表旋转操作。

在算法设计上，首先定义len变量求出链表长度；其次将尾结点next指针指向首节点，形成一个环，接着往后移动len-k步；最后从移动后位置断开，即为所求的链表结果。
