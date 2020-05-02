# Same Tree

## 问题分析
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。


## 代码实现
``` C
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    if (p == NULL&&q == NULL)  return true;
	if ((p == NULL&&q != NULL) || (p != NULL&&q == NULL)) return false;
	if (p->val == q->val)
		return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
	else return false;
}
```

## 总结体会
本题考察结构体对成员的访问，起初访问成员使用p.val方式报错，了解到定义的结构体是指针，访问成员应用p->val方式，当定义的结构体是结构体变量是访问成员才为p.val方式。

同时应考虑到，p和q为空的情况，先进行判断，然后再用递归方式对树的结构和数值进行判断，如果相同则返回true，否则false。



