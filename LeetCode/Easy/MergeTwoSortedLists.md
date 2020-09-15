# Merge Two Sorted Lists

## 问题分析

Merge two sorted linked lists and return it as a new list.　The new list should be made by splicing together the nodes of the first two lists.

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

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
struct ListNode* mergeTwoLists(struct ListNode* l1,struct ListNode* l2)
{
	if (!l1 && !l2)  return NULL;
	   else if (!l1 && l2)  return l2;
	   else if (l1 && !l2)return l1;
	struct ListNode *Temp1 = l1;
	struct ListNode *Temp2 = l2;
	struct ListNode *head = NULL;
	struct ListNode *point = NULL;

	while (Temp1&&Temp2) {
		if (head == NULL) {
			if (Temp1->val <= Temp2->val) {
				point = Temp1;
				head = point;
				Temp1 = Temp1->next;
				point->next = NULL;
			    }
			else {
				point = Temp2;
				head = point;
				Temp2 = Temp2->next;
				point->next = NULL;
			    }
		    }
		else {
			if (Temp1->val >= Temp2->val) {
				point->next = Temp2;
				point = point->next;
				Temp2 = Temp2->next;
				point->next = NULL;
			    }
			else {
				point->next = Temp1;
				point = point->next;
				Temp1 = Temp1->next;
				point->next = NULL;
			    }
		    }
	   }
	if (Temp1) point->next = Temp1;
	if (Temp2) point->next = Temp2;
	return head;
}
```

2.递归法
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def recursive(ln1,ln2):
            if not ln1: return ln2
            if not ln2: return ln1
            if ln1.val < ln2.val:
                ln1.next = recursive(ln1.next,ln2)
                return ln1
            else:
                ln2.next = recursive(ln1,ln2.next)
                return ln2
        return recursive(l1,l2)
```

3.递归法优化代码
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def recursive(ln1,ln2):
            if not (ln1 and ln2): return ln2 or ln1
            if ln1.val < ln2.val:
                ln1.next = recursive(ln1.next,ln2)
                return ln1
            ln2.next = recursive(ln1,ln2.next)
            return ln2
        return recursive(l1,l2)
```

## 总结体会

本题考察C语言链表操作，熟悉链表元素的头指针、节点的数据域和尾节点等。

在算法实现方面，首先需要考虑到链表为空的情况，增强程序的鲁棒性；其次选出链表中最小的节点，然后遍历链表节点数据域，从小到大排序，实现要求。

递归法，在递归时注意返回的内容是同秩的，比如返回的都是listnode。