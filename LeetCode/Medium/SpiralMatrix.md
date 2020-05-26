#  Spiral Matrix

## 问题分析

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

## 代码实现

1.
``` C++
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        drt = vector<vector<int>>{{0,1},{1,0},{-1,0},{0,-1}};
        mark = vector<vector<bool>>(100,vector<bool>(100,false));
        ret.clear();  
        if(!matrix.size() || !matrix[0].size())
            return ret;
        dfs(matrix, 0, 0, -1);
        return ret;
    }
    void dfs(vector<vector<int>> & matrix, int direct, int x, int y)
    {
        for(int i = 0; i < 4; ++i){
            int j = (direct + i) % 4;
            int tx = x + drt[j][0];
            int ty = y + drt[j][1];
            if(tx >= 0 && tx < matrix.size() &&
                ty >= 0 && ty < matrix[0].size() &&
                mark[tx][ty] == false){
                mark[tx][ty] = true;
                ret.push_back(matrix[tx][ty]);
                dfs(matrix, j, tx, ty);
            }
        }
    }
private:
    vector<vector<int>> drt;
    vector<vector<bool>> mark;
    vector<int> ret;
};
```

2.
```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: 
            return [] 
        R, C = len(matrix), len(matrix[0]) 
        seen = [[False] * C for _ in matrix] 
        ans = [] 
        dr = [0, 1, 0, -1] 
        dc = [1, 0, -1, 0] 
        r = c = di = 0 
        for _ in range(R * C): 
            ans.append(matrix[r][c]) 
            seen[r][c] = True 
            cr, cc = r + dr[di], c + dc[di] 
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]: 
                r, c = cr, cc 
            else: 
                di = (di + 1) % 4 
                r, c = r + dr[di], c + dc[di] 
        return ans

```

## 总结体会

本题要求代码实现矩阵旋转。

在算法设计上，将打印过程看成：输出矩阵的第一行，然后删除第一行并将矩阵向左旋转90°，再输出矩阵第一行，然后再删除第一行并将矩阵向左旋转90°，就这样直到矩阵中的元素都被删完结束遍历。

直觉
绘制螺旋轨迹路径，我们发现当路径超出界限或者进入之前访问过的单元格时，会顺时针旋转方向。

算法
假设数组有 R\text{R}R 行 C\text{C}C 列，seen[r][c] 表示第 r 行第 c 列的单元格之前已经被访问过了。当前所在位置为 (r, c)，前进方向是 di。我们希望访问所有 R x C 个单元格。

当我们遍历整个矩阵，下一步候选移动位置是 (cr, cc)。如果这个候选位置在矩阵范围内并且没有被访问过，那么它将会变成下一步移动的位置；否则，我们将前进方向顺时针旋转之后再计算下一步的移动位置。
