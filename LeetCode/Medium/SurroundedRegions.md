#  Surrounded Regions

## 问题描述

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。



## 代码实现

1.DFS深度优先搜索
``` python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        r, c = len(board), len(board[0])

        def DFS(x,y):
            if not 0 <= x < r or not 0 <= y < c or board[x][y] != 'O':
                return
            
            board[x][y] = "A"
            DFS(x+1, y)
            DFS(x-1, y)
            DFS(x,y+1)
            DFS(x,y-1)

        for i in range(r):
            DFS(i, 0)
            DFS(i, c-1)

        for i in range(c-1):
            DFS(0, i)
            DFS(r-1, i)

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'A':
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

```


## 思路总结

DFS深度优先搜索：我们可以使用深度优先搜索实现标记操作。在下面的代码中，我们把标记过的字母 O 修改为字母 A。