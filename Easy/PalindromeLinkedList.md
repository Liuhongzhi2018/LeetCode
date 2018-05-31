#  Palindrome Linked List

## 问题分析
Given a singly linked list, determine if it is a palindrome.

请判断一个链表是否为回文链表。


## 代码实现
``` C
struct ListNode* temp;
bool list(struct ListNode* p);
bool isPalindrome(struct ListNode* head);

bool list(struct ListNode* p) {
    if (p == NULL) return true;
    bool isPal = list(p->next)&(temp->val == p->val);
    temp = temp->next;
    return isPal;
}
bool isPalindrome(struct ListNode* head) {
    temp = head;
    return list(head);
}
```

## 总结体会

本题要求判断给定链表是否为回文链表。

算法设计上定义temp结构体指针为全局变量，用isPalindrome返回是否为符合条件的链表，用list函数进行判断。首先判断链表是否为空，如果链表为空判断是回文链表，返回true。然后用list函数进行回文链表的判断，当isPal返回true时，则链表为满足条件链表。

需要注意的是，bool list(struct ListNode* p)要求先声明再使用，否则会报出conflicting types for list错误。