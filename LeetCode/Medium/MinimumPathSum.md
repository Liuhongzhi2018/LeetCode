#  Minimum Path Sum

## 问题分析
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

## 代码实现
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

## 总结体会

本题要求从网格中找出一条路径满足数字和最小，采用for循环遍历的方法。

在算法设计上，首先定义网格的行列分别为w和l；其次进行迭代运算，每次找到下一个值较小的行点或者列点，进行加和运算，直到遍历到最后一个网格节点。
