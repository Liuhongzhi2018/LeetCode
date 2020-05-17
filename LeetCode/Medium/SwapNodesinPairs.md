#  Swap Nodes in Pairs

## 问题分析
Given a linked list, swap every two adjacent nodes and return its head.

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

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
    ListNode* swapPairs(ListNode* head) {
     if (!head || !head->next) return head;
        ListNode *ret = head->next;
        head->next = swapPairs(head->next->next);
        ret->next = head;
        return ret;
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
    def swapPairs(self, head: ListNode) -> ListNode:
        dumb = ListNode(10086)
        dumb.next = head
        move = dumb
        def swap(pre,x1,x2):
            tmp = x2.next
            pre.next = x2
            x1.next = tmp
            x2.next = x1
        while True:
            try:
                swap(move,move.next,move.next.next)
                move = move.next.next
            except:
                break
        return dumb.next
```

## 总结体会

本题要求将所给的链表，相邻节点两两交换位置，返回变换之后的新链表。

在算法设计上，首先判断链表是否为空，如是则返回头节点head；其次采用递归遍历到最后一个节点，然后从后开始向前相邻两两交换；最后返回生成的链表。

方法二，首先用dumb作为假的指针头，定义一个swap function用于指针的交换；移动move指针用于指针的两两交换；采用try exception的方式，用处在于如果出现错误则跳到except，省去if和else操作。