# 序列化二叉树


## 题目描述


请实现两个函数，分别用来序列化和反序列化二叉树

二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

例如，我们可以把一个只有根节点为1的二叉树序列化为"1,"，然后通过自己的函数来解析回这个二叉树


## 代码实现

1. 前序遍历法
```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        retList = []
        def preOrder(root): # 前序遍历序列化 
            if root == None: 
                return retList.append('#') 
            retList.append(str(root.val)) 
            preOrder(root.left) 
            preOrder(root.right) 
        preOrder(root) 
        return ' '.join(retList)

    def Deserialize(self, s):
        # write code here
        retList = s.split() # 切片得到序列 
        def depreOrder(): 
            if retList == []: 
                return None 
            rootVal = retList[0] 
            del retList[0] 
            if rootVal == '#': 
                return None 
            node = TreeNode(int(rootVal)) 
            node.left = depreOrder()
            node.right = depreOrder() 
            return node 
        pRoot = depreOrder() 
        return pRoot
```
运行时间：23ms

占用内存：5860k




## 思路总结

