#  Pacific Atlantic Water Flow

## 问题描述

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.

给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。

规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。

请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。

提示：

输出坐标的顺序不重要
m 和 n 都小于150



## 代码实现

1.深入优先搜索
``` python
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        step = [[-1,0],[0,-1],[1,0],[0,1]]
        res = []
        row = len(matrix)
        col = len(matrix[0])
        q_flag = [[False]*col for _ in range(row)]
        a_flag = [[False]*col for _ in range(row)]

        def DFS(i, j, visited):
            visited[i][j] = True
            for x, y in step:
                tmp_i, tmp_j = i+x, j+y
                if tmp_i < 0 or tmp_i >= row or tmp_j < 0 or tmp_j >= col or matrix[tmp_i][tmp_j] < matrix[i][j] or visited[tmp_i][tmp_j]:
                    continue
                DFS(tmp_i, tmp_j, visited)

        for m in range(row):
            DFS(m, 0, q_flag)
            DFS(m, col-1, a_flag)
        for n in range(col):
            DFS(0, n, q_flag)
            DFS(row-1, n, a_flag)
        for i in range(row):
            for j in range(col):
                if q_flag[i][j] and a_flag[i][j]:
                    res.append([i,j])
        return res
```


## 思路总结

可以用DFS和BFS,这里用DFS  
首先,我们要找的既能流进太平洋,又能流进大西洋的,所以,我们分开讨论,找可以流进太平洋的坐标,再找大西洋的坐标。  
其次,我们不需要一个一个坐标判断,我们只要考虑边界就行,我拿上边界为例,上边界都可以流入太平洋,所以我们可以从上边界进行深度遍历,就是找比它水位高的坐标,都可以流到它这里。  
最后,我们把这上下左右四个边界都考虑一下。