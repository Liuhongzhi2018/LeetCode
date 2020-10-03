# Symmetric Tree

## 问题分析

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

给定一个二叉树，检查它是否是镜像对称的。


## 代码实现

1.
``` C
/**
* Definition for a binary tree node.
* struct TreeNode {
*     int val;
*     struct TreeNode *left;
*     struct TreeNode *right;
* };
*/
bool isSymmetric(struct TreeNode* root);
bool recursion(struct TreeNode* p, struct TreeNode* q);

bool isSymmetric(struct TreeNode* root) {
    if (root == NULL)  return true;
    return recursion(root->left, root->right);
}

bool recursion(struct TreeNode* p, struct TreeNode* q) {
    if (p == NULL&&q == NULL) return true;
    if ((p == NULL&&q != NULL) || (p != NULL&&q == NULL))  return false;
    else return (p->val == q->val) && recursion(p->right, q->left) && recursion(p->left, q->right);
}
```

2.
```python

```

## 总结体会
本题利用Same tree题目所应用的结构体知识，判断二叉树是否镜像对称，本题不同之处在于只有一个指针用于判断元素是否满足条件，需要转换为类似两个二叉树的比较。

其次采用递归函数进行判断，函数与same tree的判断方法相似，不同在于一个二叉树的左子树和另一个二叉树的右子树进行比较，满足镜像对称则返回true，否则false。

但是第一次编译时，Compile Error提示conflicting types for 'recursion'，因此在函数前先进行声明，OJ通过Accepted。




