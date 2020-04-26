# 二叉树的下一个结点


## 题目描述


给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

## 代码实现

1. 递归法
```python
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right:
            tmpNode = pNode.right
            while tmpNode.left:
                tmpNode = tmpNode.left
            return tmpNode
        else:
            tmpNode = pNode
            while tmpNode.next:
                if tmpNode.next.left == tmpNode:
                    return tmpNode.next
                tmpNode = tmpNode.next
        return None
```
运行时间：31ms

占用内存：5864k



## 思路总结

首先，寻找右子树，如果存在就一直找右子树的最左边就是下一个结点；  
其次，没有右子树，寻找父结点，一直找到父结点的左子树，打印父结点。