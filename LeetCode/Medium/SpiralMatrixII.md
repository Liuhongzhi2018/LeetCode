#  Spiral MatrixII

## 问题分析
Given a positive integer n, generate a square matrix filled with elements from 1 to n<sup>2</sup> in spiral order.

给定一个正整数 n，生成一个包含 1 到 n<sup>2</sup> 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

## 代码实现
1. 
``` C++
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>>matrix(n,vector<int>(n));
        int rows=0,rowe=n-1;
        int cols=0,cole=n-1;
        int i,cnt=1;
        while(rows<=rowe&&cols<=cole){
            for(i=cols;i<=cole;i++)  matrix[rows][i]=cnt++;
            rows++;

            for(i=rows;i<=rowe;i++)  matrix[i][cole]=cnt++;
            cole--;

            for(i=cole;i>=cols;i--)  matrix[rowe][i]=cnt++;
            rowe--;

            for(i=rowe;i>=rows;i--)  matrix[i][cols]=cnt++;
            cols++;
        }
     return matrix;
    }
};
```


2. 
```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        res[0] = list(range(1,n+1))
        cur, length = n+1, n-1
        x, y = 0, n-1
        while length > 0:
            # go down then left
            for i in range(length):
                x += 1
                res[x][y], cur = cur, cur+1
            for j in range(length):
                y -= 1
                res[x][y], cur = cur, cur+1

            length -= 1
            # go up then right
            for i in range(length):
                x -= 1
                res[x][y], cur = cur, cur+1
            for j in range(length):
                y += 1
                res[x][y], cur = cur, cur+1
            length -= 1

        return res

```

## 总结体会

本题要求根据给定的正整数生成的n<sup>2</sup>元素组成螺旋矩阵。

在算法设计上，首先创建一个二维数组matrix，用来保存生成的矩阵元素，声明变量i用来指向矩阵位置；其次从第1行1列开始在同一行保存元素1到n，然后是第n列第1行同一列，再从第n列第n行向第1列，其次是第n行1列向第1行依次保存到n<sup>2</sup>；最后返回matrix即为所求的矩阵。

当排完第一行元素到右上角，之后一个明显的规律是，经过四次回到右上角，边长会变化两次。
