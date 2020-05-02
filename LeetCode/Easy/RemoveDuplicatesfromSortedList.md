# Remove Duplicates from Sorted List

## 问题分析
Given a sorted linked list, delete all duplicates such that each element appear only once.

给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。


## 代码实现
``` C
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
  if (head == NULL || head->next == NULL) return head;
	struct ListNode* p = head;
	while (head->next!= NULL) {
		if (head->val == head->next->val)
			head->next = head->next->next;
		else
			head = head->next;
	}
	return p;
}
```

## 总结体会
本题主要考察单向链表基本操作中的删除元素。

首先如果是空链表或者链表只有头结点，则返回链表指针，否则首先将头结点用P指针保存。

其次进行判断，如果前驱结点的值与后继结点的值相等，则将前驱next指向后继next，否则指向下一个结点进行判断。

最后当链表遍历完成，则将P指针指向的结点返回。


