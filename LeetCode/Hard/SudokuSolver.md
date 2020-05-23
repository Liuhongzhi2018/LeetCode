#   Sudoku Solver

## 问题分析

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Empty cells are indicated by the character '.'.

编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

    数字 1-9 在每一行只能出现一次。
    数字 1-9 在每一列只能出现一次。
    数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

空白格用 '.' 表示。



## 代码实现

1.
```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r3, r9, s9 = range(3),range(9),set(str(x) for x in range(1,10))
        def dfs():
            for i, row in enumerate(board):
                for j,char in enumerate(row):
                    if char != '.':
                        continue
                    for x in s9-{row[k] for k in r9}-{board[k][j] for k in r9} - \
                    {board[i//3*3+m][j//3*3+n] for m in r3 for n in r3}:
                        board[i][j] = x
                        if dfs():
                            return True
                        board[i][j] = '.'
                    return False
            return True
        dfs()
```

2.
```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.sets = self.valid()
        self.solve()
        return self.board

    def valid(self):
        sets = {}
        board = self.board
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue
                val = {str(x+1) for x in range(9)}
                sets[(i,j)] = val - {board[i][y] for y in range(9)} - \
                {board[y][j] for y in range(9)} - \
                {board[ii+(i-i%3)][jj+(j-j%3)] for ii in range(3) for jj in range(3)}
        return sets

    def solve(self):
        if len(self.sets)==0:
            return True
        nex = min(self.sets.keys(),key = lambda x:len(self.sets[x]))
        for d in self.sets[nex]:
            update = {nex:self.sets[nex]}
            if self.oneval(nex,d,update) and self.solve():
                return True
            self.undo(nex,update)
        return False
    
    def oneval(self,position,char,update):
        x,y = position
        self.board[x][y] = char
        self.sets.pop(position)
        for i,j in self.sets.keys():
            if char in self.sets[(i,j)]:
                if i==x or j==y or (x//3,y//3)==(i//3,j//3):
                    update[(i,j)] = char
                    self.sets[(i,j)].remove(char)
                    if len(self.sets[(i,j)]) == 0:
                        return False
        return True

    def undo(self,position,update):
        x,y=position
        self.board[x][y] = '.'
        for pos in update.keys():
            if pos not in self.sets:
                self.sets[pos] = update[pos]
            else:
                self.sets[pos].add(update[pos])
        return None

```

## 思路总结

方法一思路简单。顺序找每一个空格，然后将空格的可能性列举出来，并且一个个去尝试，直到最终填补完所有的可能性。


方法二比较快。引入可能性这个因素，会减少其他空格的可能性。第一个函数是主函数，通过组合下面四个函数完成解数独的任务；valid用于初始化时每一格可以有效的字符是哪一些；solve用于解数独，主要操作函数；oneval用于更新选中的某一种情况，其他格子的情况；如果行不通时需要重新更新可能性。