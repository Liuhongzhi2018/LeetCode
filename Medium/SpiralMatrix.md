#  Spiral Matrix

## 问题分析
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

## 代码实现
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

## 总结体会

本题要求代码实现矩阵旋转。

在算法设计上，将打印过程看成：输出矩阵的第一行，然后删除第一行并将矩阵向左旋转90°，再输出矩阵第一行，然后再删除第一行并将矩阵向左旋转90°，就这样直到矩阵中的元素都被删完结束遍历。
