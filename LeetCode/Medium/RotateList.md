#  Rotate List

## 问题描述

Given a linked list, rotate the list to the right by k places, where k is non-negative.

给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

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

2.
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # base cases 
        if not head: 
            return None 
        if not head.next: 
            return head 
            
        # close the linked list into the ring
        old_tail = head 
        n = 1 
        while old_tail.next: 
            old_tail = old_tail.next 
            n += 1 
        old_tail.next = head 
        
        # find new tail : (n - k % n - 1)th node 
        # and new head : (n - k % n)th node 
        new_tail = head 
        for i in range(n - k % n - 1): 
            new_tail = new_tail.next 
        new_head = new_tail.next 
            
        # break the ring 
        new_tail.next = None 
        return new_head
```

## 思考总结

本题要求根据给定的旋转链表，向右旋转k步，进行链表旋转操作。

在算法设计上，首先定义len变量求出链表长度；其次将尾结点next指针指向首节点，形成一个环，接着往后移动len-k步；最后从移动后位置断开，即为所求的链表结果。

链表中的点已经相连，一次旋转操作意味着：  
先将链表闭合成环  
找到相应的位置断开这个环，确定新的链表头和链表尾。

