#  Max Area of Island

## 问题描述

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

给定一个包含了一些 0 和 1 的非空二维数组 grid 。

一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)


## 代码实现

1.DFS深度优先搜索
``` python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) 
        
        def dfs(gird, i, j): 
            if 0<=i<m and 0<=j<n and grid[i][j]: 
                grid[i][j] = 0 
                return 1 + dfs(grid, i+1,j) + dfs(grid, i-1, j) + dfs(grid, i, j+1) + dfs(grid, i, j-1) 
            return 0 

        result = 0 
        for x in range(m): 
            for y in range(n): 
                result = max(result, dfs(grid, x, y)) 
        return result
```

2.
```python
class Solution:
    def dfs(self, grid, cur_i, cur_j): 
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
            return 0 
        grid[cur_i][cur_j] = 0 
        ans = 1 
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i, next_j = cur_i + di, cur_j + dj 
            ans += self.dfs(grid, next_i, next_j) 
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid): 
             for j, n in enumerate(l): 
                ans = max(self.dfs(grid, i, j), ans)
        return ans
```


## 思考总结

算法  
我们通过网格中每个连通形状的面积，然后取最大值。  
如果我们在一个土地上，以 4 个方向探索与之相连的每一个土地（以及与这些土地相连的土地），那么探索过的土地总数将是该连通形状的面积。  
为了确保每个土地访问不超过一次，我们每次经过一块土地时，将这块土地的值置为 0。这样我们就不会多次访问同一土地。
