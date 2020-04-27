# 二叉搜索树的第k个结点


## 题目描述

给定一棵二叉搜索树，请找出其中的第k小的结点。例如，（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。

## 代码实现

1. 中序遍历法
```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        
        retList = []
        
        def preOrder(pRoot):
            if pRoot == None:
                return None
            preOrder(pRoot.left)
            retList.append(pRoot)
            preOrder(pRoot.right)
            
        preOrder(pRoot)
        if len(retList) < k or k < 1:
            return None
        
        return retList[k-1]
```
运行时间：27ms

占用内存：5704k



## 思路总结

二叉搜索树，左子树都比根结点小，右子树都比根结点大。

中序遍历是从小到大排序的，找第k元素就可以。