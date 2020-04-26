# 二叉搜索树与双向链表


## 题目描述

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

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
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return None
        
        def find_right(node):
            while node.right:
                node = node.right
            return node
        
        # 左、右子树
        leftNode = self.Convert(pRootOfTree.left)
        rightNode = self.Convert(pRootOfTree.right)
        
        # 记录最终输出链表的头结点，只为输出
        retNode = leftNode
        
        # 处理左子树
        if leftNode:
        # 找到左子树的双向链表的最后一个结点
            leftNode = find_right(leftNode)
        else:
            retNode = pRootOfTree
            
        # 将根节点指向左子树链表的最后一个结点和右子树链表的第一个结点
        pRootOfTree.left = leftNode
        pRootOfTree.right = rightNode
        
        # 另一个方向的链接，将左子树链表的最后一个节点指向根节点，将右子树链表的第一个节点指向根节点
        if leftNode != None:
            leftNode.right = pRootOfTree
        if rightNode != None:
            rightNode.left = pRootOfTree
        return retNode

```
运行时间：24ms

占用内存：5864k


2. 中序遍历法
```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree: 
            return 
        self.mid = [] 
        self.middle(pRootOfTree)
        for i in range(len(self.mid)-1):
            self.mid[i].right = self.mid[i+1]
            self.mid[i+1].left = self.mid[i]
        return self.mid[0] 
        
    def middle(self, root): 
        if not root: 
            return 
        self.middle(root.left) 
        self.mid.append(root) 
        self.middle(root.right)
```
运行时间：23ms

占用内存：5860k


## 思路总结

将根结点连到左子树的最右和右子树的最左。  
然后增加双向链接。