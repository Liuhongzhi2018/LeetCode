# 二叉树中和为某一值的路径


## 题目描述


输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)


## 代码实现

1. 广度优先遍历
```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root == None:
            return []
        ret = [] 
        supportArrayList = [[root.val]] # 对于每个节点来说，保存其路径，保存的是node的值
        support = [root] # 当前的node,保存的是node，用来做广度优先遍历
        
        while support:
            tmpNode = support[0]
            tmpArrayList = supportArrayList[0] 
            if tmpNode.left == None and tmpNode.right == None:
                if sum(tmpArrayList) == expectNumber:
                    ret.insert(0, tmpArrayList)
            if tmpNode.left:
                support.append(tmpNode.left)
                newTmpArrayList = copy.copy(tmpArrayList)
                newTmpArrayList.append(tmpNode.left.val)
                supportArrayList.append(newTmpArrayList)
            if tmpNode.right:
                support.append(tmpNode.right)
                newTmpArrayList = copy.copy(tmpArrayList)
                newTmpArrayList.append(tmpNode.right.val)
                supportArrayList.append(newTmpArrayList)
                
            del supportArrayList[0] 
            del support[0]
        return ret
```
运行时间：21ms

占用内存：5848k



## 思路总结

首先，判断是否为空；  
其次，声明2个列表，一个是保存结点值；一个是保存结点，用于广度优先遍历；
然后，如果遍历到根结点，判断是和是否为所求值，进行返回。