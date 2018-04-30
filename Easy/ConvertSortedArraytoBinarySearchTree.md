#  Convert Sorted Array to Binary Search Tree

## 问题分析
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。


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
 struct TreeNode* Tree(int* nums, int left, int right)
 {
     if (left <= right) {
         int mid = (left + right) / 2;
         struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
         root->val = nums[mid];
         root->left = Tree(nums, left, mid - 1);
         root->right = Tree(nums, mid + 1, right);
         return root;
     }
     else return 0;
 }

 struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
     return Tree(nums, 0, numsSize - 1);
 }
```

## 总结体会
本题要求高度平衡的二叉搜索树，左右子树高度差不超过1，可以转换为二分查找的问题，从而可实现左右子树平衡的要求。

当有序数组的最小值不大于最大值时，满足二分查找算法的条件，采用递归算法，求出二分查找树，返回根结点；否则返回0。






