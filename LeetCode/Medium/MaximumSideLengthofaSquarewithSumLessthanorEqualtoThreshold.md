#  Maximum Side Length of a Square with Sum Less than or Equal to Threshold

## 问题描述

Given a m x n matrix mat and an integer threshold. Return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。

请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。


## 代码实现

1.二分查找
```python
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        P = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1]

        def getRect(x1, y1, x2, y2): 
            return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]

        l, r, ans = 1, min(m,n), 0
        while l<=r:
            mid = l + (r-l) // 2
            find = any(getRect(i, j, i + mid - 1, j + mid - 1) <= threshold for i in range(1, m - mid + 2) for j in range(1, n - mid + 2))
            if find:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
```


## 思路总结

我们首先计算出数组 mat 的前缀和数组 P，随后依次枚举 mat 中的正方形，计算出每个正方形的元素之和。具体地，当数组 mat 的大小为 m * n 时，正方形的左上角可以是 mat 中的任意位置，边长不会超过 m 和 n 中的较小值 min(m, n)，这样我们就可以使用三重循环枚举所有的正方形，时间复杂度为 O(MN∗min⁡(M,N))O(MN * \min(M, N))O(MN∗min(M,N))。由于我们可以借助数组 P 在 O(1)O(1)O(1) 的时间计算任意正方形的元素之和，因此该算法的总时间复杂度为 O(MN∗min⁡(M,N))O(MN * \min(M, N))O(MN∗min(M,N))。

若使用 C++ 语言编写上述算法，则可以恰好在规定时间内通过所有测试数据，但对于 Python 语言则无法通过。因此我们必须对该算法进行优化。

由于数组 mat 中的所有元素均为非负整数，因此若存在一个边长为 c 且元素之和不超过阈值的正方形，那一定存在一个边长为 1, 2, ..., c - 1 且元素之和不超过阈值的正方形（在边长为 c 的正方形内任取一个边长为 1, 2, ..., c - 1 的正方形即可）。这样我们可以使用二分查找的方法，找出最大的边长 c。二分查找的上界为 min(m, n)，下界为 1，在二分查找的过程中，若当前查找的边长为 c'，我们只需要枚举 mat 中所有边长为 c' 的正方形，并判断其中是否存在一个元素之和不超过阈值的正方形即可。

复杂度分析

    时间复杂度：O(MN∗log⁡min⁡(M,N))O(MN * \log\min(M, N))O(MN∗logmin(M,N))。二分查找的次数为 O(log⁡min⁡(M,N))O(\log\min(M, N))O(logmin(M,N))，在每次二分查找中，需要枚举所有边长为 c' 的矩形，数量为 O(MN)O(MN)O(MN)，因此总时间复杂度为 O(MN∗log⁡min⁡(M,N))O(MN * \log\min(M, N))O(MN∗logmin(M,N))。

    空间复杂度：O(MN)O(MN)O(MN)。
