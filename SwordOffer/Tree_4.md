# 从上往下打印二叉树


## 题目描述

从上往下打印出二叉树的每个节点，同层节点从左至右打印。


## 代码实现

1. 遍历法
```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root == None:
            return []
        support = [root]
        ret = []
        while support:
            tmpNode = support[0]
            ret.append(tmpNode.val)
            if tmpNode.left:
                support.append(tmpNode.left)
            if tmpNode.right:
                support.append(tmpNode.right)
                
            del support[0]
            
        return ret
```
运行时间：23ms

占用内存：5692k



## 思路总结

从根结点找左结点，然后右结点，用列表保存结点。