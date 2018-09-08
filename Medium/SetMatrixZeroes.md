#  Set Matrix Zeroes

## 问题分析
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。

## 代码实现
``` C++
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int i,j;
        int row = matrix.size();
		if (row < 1) return;
		int col = matrix[0].size();
		vector<bool> newcol(col);
		vector<bool> newrow(row);
		for (i = 0; i < row; i++){
			for (j = 0; j < col; j++){
				if (matrix[i][j] == 0){
					newrow[i] = true;
					newcol[j] = true;
				}
			}
		}
		for (i= 0; i < row; i++){
			for (j = 0; j < col; j++){
				if (newrow[i]) matrix[i][j] = 0;
				else if (newcol[j]) matrix[i][j] = 0;
			}
        }
    }
};
```

## 总结体会

本题要求从矩阵中找出0元素，将其所在行列的元素均置0。

在算法设计上，首先遍历矩阵元素，如有0元素存在，修改所在行和列标志位均为true；其次用for循环嵌套，将所在行列的元素均原地修改为0；最后所求matrix即为所求矩阵。
