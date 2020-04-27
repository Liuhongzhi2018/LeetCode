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
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        stack1 = [pRoot]
        stack2 = []
        ret = []
        while stack1 or stack2:
            if stack1:
                tmpRet = []
                while stack1:
                    tmpNode = stack1.pop()
                    tmpRet.append(tmpNode.val)
                    if tmpNode.left:
                        stack2.append(tmpNode.left)
                    if tmpNode.right:
                        stack2.append(tmpNode.right)
                ret.append(tmpRet)

            if stack2:
                tmpRet = []
                while stack2:
                    tmpNode = stack2.pop()
                    tmpRet.append(tmpNode.val)
                    if tmpNode.right:
                        stack1.append(tmpNode.right)
                    if tmpNode.left:
                        stack1.append(tmpNode.left)
                ret.append(tmpRet)
        return ret
```

运行时间：28ms

占用内存：5972k




## 思路总结

首先，定义2个栈，并且添加初始值pRoot；  
第一行结点加入stack1，第二行结点加入stack2，第三行结点加入stack1。   