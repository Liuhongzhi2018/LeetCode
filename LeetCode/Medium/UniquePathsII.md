#  Unique Paths II

## 问题分析
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

## 代码实现
``` C++
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int i,j;
        if (obstacleGrid.empty())      return 0;
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int> > path(m, vector<int>(n, 0));
        for (i = 0; i < m; i++){
            if (obstacleGrid[i][0] != 1)
                path[i][0] = 1;
            else   break;
        }
        for (j = 0; j < n; j++){
            if (obstacleGrid[0][j] != 1)
                path[0][j] = 1;
            else  break;
        }
        for (i = 1; i < m; i++){
            for (j = 1; j < n; j++){
               if (obstacleGrid[i][j] == 1)
                    path[i][j] = 0;
                else   path[i][j] = path[i][j - 1] + path[i - 1][j];            
            }
        }
        return path[m - 1][n - 1];
    }
};
```

## 总结体会

本题要求机器人所在网格位置，求出到指定网格右下角的路径数量，与上一题不同在于网格中有障碍物，需要提前判断路径中是否有障碍物。

在算法设计上，首先定义二维向量path用来保存所求路径数；其次用for循环判断网格矩阵的首列和首行是否有障碍物；然后判断网格的其他位置是否有障碍物；最后返回path即为所求路径数。
