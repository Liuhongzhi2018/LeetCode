#  Path Sum

## 问题分析
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

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
bool hasPathSum(struct TreeNode* root, int sum) {
    if (root == NULL)  return false;
    if ((root->left == NULL) && (root->right == NULL)) { 
        if(root->val == sum)  return true; 
        else return false;
    }
    else return (hasPathSum(root->left, sum - root->val) || hasPathSum(root->right, sum - root->val));
}
```

## 总结体会
本题是已知目标和，判断是否有一条从根节点到叶子节点的路径，使得各节点值之和满足目标和。

因为求和时需要遍历二叉树各节点，所以采用递归算法，注意的是递归调用时，sum值应减去当前的节点值，然后进入下一次递归调用。当叶子节点值与sum减去路径各节点值后的数值相等，返回true。

第一次编译错误是由于二叉树为[]且sum==0，判断为true。按照题目要求返回应为false。因为在条件判断时，我将root==NULL且sum==0返回true，修改为false后accepted。









