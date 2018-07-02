#  Sum of Left Leaves

## 问题分析
Find the sum of all left leaves in a given binary tree.

计算给定二叉树的所有左叶子之和。

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
int sumOfLeftLeaves(struct TreeNode* root) {
    if(!root) return 0;
    if(root->left&&!root->left->left&&!root->left->right) 
        return root->left->val + sumOfLeftLeaves(root->right);
    return sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right);
}
```

## 总结体会

本题要求在所给的二叉树中，找出所有左叶子结点并进行求和。

在算法设计上，首先判断二叉树是否为空；其次找出左叶子结点，满足左叶子的条件是结点非空且没有子结点，并进行求和运算；最后运用迭代法返回求出的左叶子之和。

