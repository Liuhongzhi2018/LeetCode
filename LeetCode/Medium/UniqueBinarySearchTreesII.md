#   Unique Binary Search Trees II

## 问题描述

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

## 代码实现

1.
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def generateTrees(start, end):
            if start > end:
                return [None,]
        
            alltree = []
            for i in range(start, end+1):
                lefttree = generateTrees(start, i-1)
                righttree = generateTrees(i+1,end)

                for l in lefttree:
                    for r in righttree:
                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r
                        alltree.append(cur)

            return alltree

        return generateTrees(1,n) if n else []
            
```


## 思路总结

二叉搜索树关键的性质是根节点的值大于左子树所有节点的值，小于右子树所有节点的值，且左子树和右子树也同样为二叉搜索树。因此在生成所有可行的二叉搜索树的时候，假设当前序列长度为 nnn，如果我们枚举根节点的值为 iii，那么根据二叉搜索树的性质我们可以知道左子树的节点值的集合为 [1 … i−1]，右子树的节点值的集合为 [i+1 … n]。而左子树和右子树的生成相较于原问题是一个序列长度缩小的子问题，因此我们可以想到用递归的方法来解决这道题目。

我们定义 generateTrees(start, end) 函数表示当前值的集合为 [start,end]，返回序列 [start,end] 生成的所有可行的二叉搜索树。按照上文的思路，我们考虑枚举 [start,end]中的值 i 为当前二叉搜索树的根，那么序列划分为了 [start,i−1] 和 [i+1,end] 两部分。我们递归调用这两部分，即 generateTrees(start, i - 1) 和 generateTrees(i + 1, end)，获得所有可行的左子树和可行的右子树，那么最后一步我们只要从可行左子树集合中选一棵，再从可行右子树集合中选一棵拼接到根节点上，并将生成的二叉搜索树放入答案数组即可。

递归的入口即为 generateTrees(1, n)，出口为当 start>end\textit{start}>\textit{end}start>end 的时候，当前二叉搜索树为空，返回空节点即可。