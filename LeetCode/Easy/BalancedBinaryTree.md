#  Balanced Binary Tree

## 问题分析
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as: a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。


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
int height(struct TreeNode* root);
bool isBalanced(struct TreeNode* root);

int max(int a, int b) {
    int max = 0;
    if (a > b) max = a;
    else  max = b;
    return max;
}

int height(struct TreeNode* root) {
    if (root == NULL)  return 0;
    return max(height(root->left), height(root->right))+1;
}

bool isBalanced(struct TreeNode* root) {
    int sign = 1;
    if (root == NULL)  return true;
    if (height(root->left) - height(root->right) > 1 || height(root->left) - height(root->right) < -1)
        sign = 0;
    return sign&&isBalanced(root->left) && isBalanced(root->right);
}
```

## 总结体会
本题是判断高度平衡的二叉树，在算法设计上沿用在Maximum Depth of Binary Tree题目中的求二叉树深度的方法，与之不同的是本题要对深度进行判断，所给二叉树是否满足高度平衡二叉树的条件。

在isBalanced函数中，取sign为标志位，如果左右子树高度绝对值超过1则不满足条件，sign修改为0；同样由二叉树的递归定义，采用递归算法，对二叉树各结点遍历，若左右子树的深度满足条件，即为所求的二叉树。






