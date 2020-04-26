# 按之字形顺序打印二叉树


## 题目描述

请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

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
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot == None: 
                return True 
            
        def isMirror(left,right):
            if left == None and right == None: 
                return True 
            if left == None or right == None: 
                return False 
            if left.val != right.val: 
                return False 

            ret1 = isMirror(left.left,right.right) 
            ret2 = isMirror(left.right,right.left) 
            return ret1 and ret2 
        return isMirror(pRoot.left,pRoot.right)
```
运行时间：21ms

占用内存：5728k



## 思路总结

一个二叉树和二叉树的镜像相同，左子树等于右子树，左子树根结点的左结点等于右子树根结点的右结点。