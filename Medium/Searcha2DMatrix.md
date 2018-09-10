#  Search a 2D Matrix

## 问题分析
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties: Integers in each row are sorted from left to right. The first integer of each row is greater than the last integer of the previous row.

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：每行中的整数从左到右按升序排列。每行的第一个整数大于前一行的最后一个整数。

## 代码实现
``` C++
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty()) return false;
        int m = matrix.size(), n = matrix.front().size();
        int begin = 0, middle, end = m * n;
        int row, col;
        while(begin < end){
            middle = begin + (end - begin) / 2;
            row = middle / n;
            col = middle % n;
            if(matrix[row][col] == target)  return true;
            else if(matrix[row][col] < target)  begin = middle + 1;
            else end = middle;
        }
        return false;
    }
};
```

## 总结体会

本题要求从所给要求的矩阵中确定是否含有指定目标值。

在算法设计上，首先将矩阵的行列赋值给定义变量m,n；其次采用二分查找法，确定矩阵储存的二维数组中是否含有目标值；最后如果查找结束没有找到目标值则返回false。
