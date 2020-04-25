# 二叉树的镜像


## 题目描述

操作给定的二叉树，将其变换为源二叉树的镜像。


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
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return None
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
```
运行时间：23ms

占用内存：5736k



## 思路总结

首先，处理根结点；  
然后，处理左子树和右子树。