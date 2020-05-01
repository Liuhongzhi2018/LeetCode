#  平衡二叉树


## 题目描述


输入一棵二叉树，判断该二叉树是否是平衡二叉树。

在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树


## 代码实现

1. 递归法
```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        if abs(self.max_depth(pRoot.left) - self.max_depth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    def max_depth(self, pRoot):
        if not pRoot:
            return 0 
        return max(self.max_depth(pRoot.left), self.max_depth(pRoot.right)) + 1
```
运行时间：22ms

占用内存：5856k






## 思路总结

