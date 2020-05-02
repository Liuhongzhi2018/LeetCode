# Maximum Depth of Binary Tree

## 问题分析
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。


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
int max(int a, int b);
int maxDepth(struct TreeNode* root);

int max(int a, int b) {
    int max = 0;
    if (a > b) max = a;
    else  max = b;
    return max;
}

int maxDepth(struct TreeNode* root) {
    if (root == NULL)  return 0;
    else return max(maxDepth(root->left), maxDepth(root->right)) + 1;
}
```

## 总结体会
本题考察对二叉树结点的遍历，直到查找结点为NULL，可求得二叉树的深度。

算法设计上沿用递归算法，先求得左子树的深度，然后求得右子树的深度，比较得到二者的最大值加1，可以求出二叉树的最大深度。

需要注意的是，运用递归算法时需要仔细考虑用到的函数及需要返回的值，抓住重复计算的过程进行递归运算。




