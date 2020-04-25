# 二叉搜索树的后序遍历序列


## 题目描述

输入一个非空整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

## 代码实现

1. 递归法
```python
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == []:
            return False
        rootNum = sequence[-1]
        del sequence[-1]
        index = None
        for i in range(len(sequence)):
            if not index and sequence[i] > rootNum:
                index = i
            if index != None and sequence[i] < rootNum:
                return False
        
        if sequence[:index] == []:
            leftret = True
        else:
            leftret = self.VerifySquenceOfBST(sequence[:index])
        if sequence[index:-1] == []:
            rightret = True
        else:
            rightret = self.VerifySquenceOfBST(sequence[index:-1])
        
        return leftret and rightret
```
运行时间：23ms

占用内存：5860k



## 思路总结

二叉查找树（Binary Search Tree），（又：二叉搜索树，二叉排序树）它或者是一棵空树，或者是具有下列性质的二叉树： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。二叉搜索树作为一种经典的数据结构，它既有链表的快速插入与删除操作的特点，又有数组快速查找的优势；所以应用十分广泛，例如在文件系统和数据库系统一般会采用这种数据结构进行高效率的排序与检索操作。

此题二叉查找树不能为空，但是结点可以为空。  
分别处理root，left，right结点。