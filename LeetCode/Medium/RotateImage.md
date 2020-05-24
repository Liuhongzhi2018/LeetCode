#  Rotate Image

## 问题分析

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

## 代码实现

1.
``` C++
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int lr=0,lc=0;
        int rr=matrix.size()-1,rc=matrix[0].size()-1;
        while(lr<rr){
            exchange(matrix,lr++,lc++,rr--,rc--);
        }

    }
    void exchange(vector<vector<int>>&matrix,int lr,int lc,int rr,int rc){
        int times=rr-lr;
        int i,tmp;
        for(i=0;i<times;i++){
            tmp=matrix[lr][lc+i];
            matrix[lr][lc+i]=matrix[rr-i][lc];
            matrix[rr-i][lc]=matrix[rr][rc-i];
            matrix[rr][rc-i]=matrix[lr+i][rc];
            matrix[lr+i][rc]=tmp;
        }
    }
};
```

2.
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start = 0
        gap = len(matrix)-1
        while gap>0:
            for i in range(gap):
                matrix[start][start+i],\
                matrix[start+i][start+gap],\
                matrix[start+gap][start+gap-i],\
                matrix[start+gap-i][start] = \
                matrix[start+gap-i][start],\
                matrix[start][start+i],\
                matrix[start+i][start+gap],\
                matrix[start+gap][start+gap-i]
            start += 1
            gap -= 2
        return matrix
```

## 总结体会

本题要求对一个二维n阶方阵保存的图像进行原地旋转，即不能额外声明矩阵空间用来保存元素。

在算法设计上，首先定义矩阵的左上角和右下角的行列坐标分别是lr,lc,rr和rc，与CV中bounding box的x,y的坐标保持一致；其次调用exchange函数进行旋转，交换矩阵中的数字，变量tmp为中间变量；根据矩阵左上角和右下角确定一圈，旋转后的matrix即为所求的旋转矩阵。
