#   N-Queens II

## 问题分析

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

## 代码实现

1.
```python
class Solution:
    vis=[0]*100
    sub=[0]*200
    add=[0]*200
    ans=0
    def totalNQueens(self, n: int) -> int:
        def dfs(i):
            if i==n+1:
                self.ans+=1
                return
            j=1
            while j<=n:
                if not self.vis[j] and not self.sub[i-j+100] and not self.add[i+j]:
                    self.vis[j]=self.sub[i-j+100]=self.add[i+j]=1
                    dfs(i+1)
                    self.sub[i-j+100]=self.add[i+j]=self.vis[j]=0
                j+=1
        dfs(1)
        return self.ans
```


## 思路总结

