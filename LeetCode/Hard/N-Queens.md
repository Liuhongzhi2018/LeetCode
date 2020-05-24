#  N-Queens 

## 问题分析

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。


## 代码实现

1.循环法
```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        n = int(n)
        result = []
        col = [-1] * n
        k = 0
        while k>=0:
            col[k] = col[k]+1 
            while col[k]<n and not self.judgePlace(k,col): 
                col[k] += 1 
            if col[k]<n:
                if k == n-1: 
                    empty = ['.'*n for i in range(0,n)] 
                    for i in range(0,n): 
                        temp = list(empty[i]) 
                        temp[col[i]] = 'Q' 
                        empty[i] = ''.join(temp) 
                    result.append(empty)
                else:
                    k += 1
                    col[k] = -1
            else:
                k -= 1
        return result

    def judgePlace(self,k,col): 
        for i in range(0,k): 
            if col[i] == col[k] or abs(col[k]-col[i]) == abs(k - i):
                return False 
        return  True

```

2.
```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        n = int(n)
        result = []
        record = [0]*(n+1)
        self.findResult(result,n,1,1,record)
        return result

    def findResult(self,result,total,row,col,record):
        if row == 0:
            return result
        record[row] = col
        while record[row]<=total and not self.judgePlace(row,record):
            record[row] += 1
        if record[row]>total: 
            row -= 1 
            newCol = record[row] + 1 
            self.findResult(result,total,row,newCol,record) 
        else: 
            if row == total: 
                empty = ['.'*total for i in range(0,total)] 
                for i in range(0,total): 
                    temp = list(empty[i]) 
                    temp[record[i+1]-1] = 'Q' 
                    empty[i] = ''.join(temp) 
                result.append(empty)
                row -= 1 
                newCol = record[row] + 1 
                self.findResult(result,total,row,newCol,record)
            else: 
                row += 1 
                self.findResult(result,total,row,1,record)

    def judgePlace(self,row,col): 
        for i in range(1,row): 
            if col[i] == col[row] or abs(col[row]-col[i]) == abs(row - i):
                return False 
        return  True

```


## 思路总结

由于每行只能有一个皇后，第一行 有N种可能，从一行一列开始 如果一行一列可以放置皇后 则找到下一行第一个能放置皇后的列。如果下一行 没有符合条件的列，就返回上一行找到下一个可以放置皇后的列。遍历的行数 == N 则获得一次 结果。如果在第一行也找不到能放置皇后的列 则查找结束。
