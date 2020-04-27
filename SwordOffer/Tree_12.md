# 把二叉树打印成多行


## 题目描述


从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。


## 代码实现

1. 队列保存法
```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        queue1 = [pRoot]
        queue2 = []
        ret = []
        while queue1 or queue2:
            if queue1:
                tmpRet = []
                while queue1:
                    tmpNode = queue1[0]
                    tmpRet.append(tmpNode.val)
                    del queue1[0]
                    if tmpNode.left:
                        queue2.append(tmpNode.left)
                    if tmpNode.right:
                        queue2.append(tmpNode.right)
                ret.append(tmpRet)
            if queue2:
                tmpRet = []
                while queue2:
                    tmpNode = queue2[0]
                    tmpRet.append(tmpNode.val)
                    del queue2[0]
                    if tmpNode.left:
                        queue1.append(tmpNode.left)
                    if tmpNode.right:
                        queue1.append(tmpNode.right)
                ret.append(tmpRet)
        return ret
```
运行时间：25ms

占用内存：5860k


## 思路总结

