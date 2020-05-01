# 顺时针打印矩阵


## 题目描述

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

## 代码实现

1. 
```python
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = [] 
        while matrix: 
            result += matrix.pop(0) 
            if matrix: 
                matrix = self.rotate(matrix) 
        return result 
            
    def rotate(self, matrix): 
        # 逆时针旋转矩阵 
        row = len(matrix) 
        col = len(matrix[0]) 
        # 存放旋转后的矩阵 
        new_matrix = [] 
        # 行列调换 
        for i in range(col): 
            new_line = [] 
            for j in range(row): 
                new_line.append(matrix[j][col-1-i]) 
            new_matrix.append(new_line) 
        return new_matrix
```
运行时间：24ms

占用内存：5856k




## 思路总结

每次打印并删除矩阵的第一行，然后将矩阵逆时针翻转90度，直至打印出全部结果
