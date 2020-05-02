#  Lowest Common Ancestor of a Binary Search Tree

## 问题分析
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为： “对于有根树T的两个结点u、v，最近公共祖先表示一个结点x，满足x是u、v的祖先且x的深度尽可能大（一个节点也可以是它自己的祖先）。”

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
void Common(struct TreeNode *root, int left, int right, struct TreeNode **node);
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q);

void Common(struct TreeNode *root, int left, int right, struct TreeNode **node) {
    if (root == NULL)  return;
    if (root->val >= left && root->val <= right) {
        *node = root;
        return;
    }
    else if (root->val > right)  Common(root->left, left, right, node);
    else if (root->val < right)  Common(root->right, left, right, node);
}
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    struct TreeNode *node = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    memset(node, 0, sizeof(struct TreeNode));
    int left, right;
    if (p->val <= q->val)
        left = p->val, right = q->val;
    else
        left = q->val, right = p->val;
    Common(root, left, right, &node);
    return node;
}
```

## 总结体会

本题要求在给定二叉树中，寻找两个节点的最近公共祖先。

算法设计上，定义node指针为待寻找的公共祖先，首先根据给定的节点，将较小值赋给left变量，将较大值赋给right变量。其次用Common函数返回公共祖先的值，最后lowestCommonAncestor返回所求最近公共祖先。