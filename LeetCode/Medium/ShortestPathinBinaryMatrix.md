#  Shortest Path in Binary Matrix

## 问题描述

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).

Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。

一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：

相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角）
C_1 位于 (0, 0)（即，值为 grid[0][0]）
C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]）
如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0）

返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。


## 代码实现

1.BFS 广度优先搜索
```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        elif n <= 2:
            return n
        queue = [(0,0,1)]
        grid[0][0] = 1
        while queue:
            i, j, step = queue.pop(0)
            for dx, dy in [(-1,-1),(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1)]:
                if i + dx == n-1 and j + dy == n-1:
                    return step + 1
                if 0 <= i + dx < n and 0 <= j + dy < n and grid[i+dx][j+dy] == 0:
                    queue.append((i+dx, j+dy, step+1))
                    grid[i+dx][j+dy] = 1
        return -1
```

2. A* Search (启发式搜索)
```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid) 
        if not grid or grid[0][0] == 1 or grid[n-1][n-1] == 1: 
            return -1 
        elif n <= 2: 
            return n 
            
        def heuristic(x, y): 
            return max(abs(n-1 - x), abs(n-1 - y)) 
            
        h = [] 
        heapq.heappush(h,(0, (0, 0, 1))) 
        visited = set() 
        while h: 
            _, (i, j, step) = heapq.heappop(h) 
            
            if (i, j) in visited: 
                continue 
            visited.add((i, j)) 
            for dx, dy in [(-1,-1), (1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1)]: 
                next_i, next_j = i+dx, j+dy 
                
                if next_i == n - 1 and next_j == n - 1:
                    return step + 1 
                    
                if 0 <= next_i < n and 0 <= next_j < n and grid[next_i][next_j] == 0: 
                    heapq.heappush(h, (step + heuristic(next_i, next_j), (next_i, next_j, step+1)))
        
        return -1
```

## 思路总结

使用标准的BFS思路，每次朝八个方向延展。很重要的一点是 要在延展的时候 就把这些被延展的点标为visited，不然会超时的。

把普通的queue改为priority queue (heapq) 然后每次优先走离终点近的点。难点是怎么定义这个优先级，这里参考：https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/solution/qi-fa-shi-sou-suo-xiao-guo-bu-cuo-by-ari-5/

通常用队列（先进先出，FIFO）实现
初始化队列Q；
Q = {起点s}；标记s为已访问；
while(Q非空):
    取Q队首元素u；u出队；
    if u == 目标状态 {...}
    所有与u相邻且未被访问的点进入队列；
    标记u为已访问；
