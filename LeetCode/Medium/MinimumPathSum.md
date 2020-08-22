#  Minimum Path Sum

## 问题分析

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

## 代码实现

1.
``` C++
class Solution {
public:
    int minPathSum(vector<vector<int> > &grid) {
    	int i,j;
        int w = grid.size();
    	int l = grid[0].size();
    	int paths[w][l];
    	paths[0][0] = grid[0][0];
 
    	for(i = 1; i < w; i++){
    		paths[i][0] = paths[i - 1][0] + grid[i][0];
    	}
    	for(j = 1; j < l; j++){
    		paths[0][j] = paths[0][j - 1] + grid[0][j];
    	}
    	for(i = 1; i < w; i++)
    		for(j = 1; j < l; j++){
    			paths[i][j] = std::min(paths[i - 1][j], paths[i][j - 1])+grid[i][j];
    		}
    	return paths[w - 1][l - 1];
    }
};
```

2.动态规划
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        row, col = len(grid), len(grid[0])
        dp = [[0] * col for _ in range(row)]
        dp[0][0] = grid[0][0]

        for i in range(1,row):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, col):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, row):
            for j in range(1,col):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[row - 1][col - 1]
```

## 总结体会

本题要求从网格中找出一条路径满足数字和最小，采用for循环遍历的方法。

在算法设计上，首先定义网格的行列分别为w和l；其次进行迭代运算，每次找到下一个值较小的行点或者列点，进行加和运算，直到遍历到最后一个网格节点。

动态规划。由于路径的方向只能是向下或向右，因此网格的第一行的每个元素只能从左上角元素开始向右移动到达，网格的第一列的每个元素只能从左上角元素开始向下移动到达，此时的路径是唯一的，因此每个元素对应的最小路径和即为对应的路径上的数字总和。  
对于不在第一行和第一列的元素，可以从其上方相邻元素向下移动一步到达，或者从其左方相邻元素向右移动一步到达，元素对应的最小路径和等于其上方相邻元素与其左方相邻元素两者对应的最小路径和中的最小值加上当前元素的值。由于每个元素对应的最小路径和与其相邻元素对应的最小路径和有关，因此可以使用动态规划求解。  
创建二维数组 dp\textit{dp}dp，与原始网格的大小相同，dp[i][j] 表示从左上角出发到 (i,j) 位置的最小路径和。显然，dp[0][0]=grid[0][0]。对于 dp 中的其余元素，通过状态转移方程计算元素值。最后得到 dp[m−1][n−1]的值即为从网格左上角到网格右下角的最小路径和。
