# 树的子结构


## 题目描述


输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）


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
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 == None or pRoot2 == None:
            return False
        
        def hasEqual(pRoot1, pRoot2):
            if pRoot2 == None: # #若匹配的子结构的结点为空，说明已经匹配上了
                return True
            if pRoot1 == None: # 若被匹配的树A为空，而匹配的树B不为空，那么匹配直接失败
                return False
            if pRoot1.val == pRoot2.val:
                if pRoot2.left == None:
                    leftEqual = True  # 左子树匹配了
                else:
                    leftEqual = hasEqual(pRoot1.left,pRoot2.left)
                if pRoot2.right == None:
                    rightEqual = True # 右子树匹配了
                else:
                    rightEqual = hasEqual(pRoot1.right,pRoot2.right)
                return leftEqual and rightEqual
            return False
        
        if pRoot1.val == pRoot2.val:
            ret = hasEqual(pRoot1,pRoot2)
            if ret:    # #直接返回会报错 不能去掉if ret，因为根结点没有匹配上，还要匹配左子树和右子树
                return True
        
        ret = self.HasSubtree(pRoot1.left, pRoot2)  #匹配A树的左子树
        if ret:
            return True
        ret = self.HasSubtree(pRoot1.right, pRoot2) #匹配A树的左子树
        return ret
```
运行时间：21ms

占用内存：5980k



## 思路总结

首先，判断边界条件；  
其次，匹配root结点，left结点和right结点；
然后，进入判断函数，匹配root结点，left结点和right结点;
最后，都不满足返回False。