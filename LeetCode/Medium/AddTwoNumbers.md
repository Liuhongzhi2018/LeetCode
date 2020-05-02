#  Add Two Numbers

## 问题分析
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

## 代码实现
1. 
``` C
/**
* Definition for singly-linked list.
* struct ListNode {
*     int val;
*     struct ListNode *next;
* };
*/
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* q = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* p = q;
    int C = 0;
    while (l1 || l2 || C)
    {
        int sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + C;
        p->val = sum % 10;
        C = sum / 10;
        l1 = l1 ? l1->next : l1;
        l2 = l2 ? l2->next : l2;
        if (!(l1 || l2 || C))
        {
            p->next = NULL;
            return q;
        }
        p->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        p = p->next;
    }
    return q;
}
```

2. 
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        carry = 0
        dummy = ListNode(0)
        p = dummy

        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry)%10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            p = p.next

        if l2:
            while l2:
                p.next = ListNode((l2.val + carry)%10)
                carry = (l2.val + carry) // 10
                l2 = l2.next
                p = p.next
            
        if l1:
            while l1:
                p.next = ListNode((l1.val + carry)%10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
                p = p.next

        if carry == 1:
            p.next = ListNode(1)

        return dummy.next
```

## 总结体会

本题要求给定的两个逆序非空链表，相加后返回新的链表，实际上是用链表完成多位数加法运算操作，头结点是个位，最后一个结点为最高位，各位依次相加形成新链表。

在算法设计上，我首先声明两个指针和一个进位变量C；其次按照加法运算法则，遍历链表将两个链表对应元素相加，进位赋值给变量C；最后依次完成运算，将新链表头指针q返回，即为所求加和后的链表。

首先init一个node，定义一个进位carry，初始为0，dummy位是链表头指针位置；  
其次如果链表不等长时，继续对长的链表进行循环；  
最后返回头指针指向的结点。