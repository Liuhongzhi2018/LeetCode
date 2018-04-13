# Merge Two Sorted Lists

## 问题分析
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

## 代码实现
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

## 总结体会
本题考察C语言链表操作，熟悉链表元素的头指针、节点的数据域和尾节点等。

在算法实现方面，首先需要考虑到链表为空的情况，增强程序的鲁棒性；其次选出链表中最小的节点，然后遍历链表节点数据域，从小到大排序，实现要求。

