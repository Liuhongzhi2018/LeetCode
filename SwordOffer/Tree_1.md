# 重建二叉树


## 题目描述

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

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
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        if len(pre) != len(tin):
            return None
        root = pre[0]
        rootNode = TreeNode(root)
        pos = tin.index(root)
        
        tinleft = tin[:pos]
        tinright = tin[pos+1:]
        
        preleft = pre[1:pos+1]
        preright = pre[pos+1:]
        
        leftNode = self.reConstructBinaryTree(preleft, tinleft)
        rightNode = self.reConstructBinaryTree(preright, tinright)
        
        rootNode.left = leftNode
        rootNode.right = rightNode
            
        return rootNode
```
运行时间：37ms

占用内存：5732k



## 思路总结

前序遍历：根结点-左结点-右结点    
中序遍历：左结点-根结点-右结点  

二叉树左半：2-4-7，右半：3-5-6-8

首先，判断边界条件；其次，初始化树结点，切分左子树和右子树；递归求出左结点和右结点；最后返回即为重建的二叉树。