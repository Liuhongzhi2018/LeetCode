# 二叉树的深度


## 题目描述

输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。


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
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None: 
            return 0 
        lDepth = Solution.TreeDepth(self , pRoot.left)
        rDepth = Solution.TreeDepth(self , pRoot.right)
        return max(lDepth , rDepth) + 1 
```
运行时间：22ms

占用内存：5836k





## 思路总结

