#  Invert Binary Tree

## 问题分析
Invert a binary tree.

Trivia: This problem was inspired by this original tweet by Max Howell.

翻转一棵二叉树。

备注: 这个问题是受到 Max Howell 的原问题启发的。


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
struct TreeNode* invertTree(struct TreeNode* root) {
    struct TreeNode* tree;
    if(root==NULL) return root;
    tree =  invertTree(root->left);
    root->left =  invertTree(root->right);
    root->right = tree;
    return root;
}
```

## 总结体会

本题要求翻转二叉树，即要求左右子树互换，主要考察对二叉树进行的基本操作。

算法设计上首先判断是否为空二叉树，如果是直接返回结点；受交换元素的练习题启发，设一个中间二叉树结点tree，保存需互换结点root->left，然后递归调用左右互换，然后将tree赋给root->right，返回root，完成翻转二叉树的操作。