#  Number of Islands

## 问题描述

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。


## 代码实现

1.DFS
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0 
        row = len(grid) 
        col = len(grid[0]) 
        cnt = 0 
        
        def dfs(i, j): 
            grid[i][j] = "0" 
            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                tmp_i = i + x 
                tmp_j = j + y 
                if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1": 
                    dfs(tmp_i, tmp_j) 
                    
        for i in range(row): 
            for j in range(col): 
                if grid[i][j] == "1": 
                    dfs(i, j) 
                    cnt += 1 
        return cnt

```


## 总结体会

这道题，遍历 grid 当发现 1 辐射出去，找到所有 1,
所以有两种方式：DFS和BFS
还有一种通过并查集解决， 把在一起的1分为一组。

