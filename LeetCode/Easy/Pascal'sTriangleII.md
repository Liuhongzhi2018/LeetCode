#  Pascal's Triangle II

## 问题分析
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

## 代码实现
``` C
/**
* Return an array of size *returnSize.
* Note: The returned array must be malloced, assume caller calls free().
*/
int* getRow(int rowIndex, int* returnSize) {
    int left, right;
    *returnSize = rowIndex + 1;
    if (rowIndex<0) return 0;
    int* a = (int*)malloc(sizeof(int)*(rowIndex + 1));
    if (rowIndex==0){
        *a = 1;
        return a;
    }
    for (int i = 1; i <= rowIndex; i++)
    {
        a[0] = a[i] = 1;
        left = a[0];
        right = a[1];
        for (int j = 1; j<i; j++)
        {
            a[j] = left + right;
            left = right;
            right = a[j + 1];
        }
    }
    return a;
}
```

## 总结体会

本题要求杨辉三角的指定行的元素，与上一题需要二维数组不同，只需将指定行元素保存到一维数组中，返回数组指针。

当所求的rowIndex行小于0时，返回的数组为0。当numRows大于等于0时，第0行已知为1，其后一行各元素是肩上两元素之和，依此类推求出该行的各元素。

需要注意的是，与上一题Pascal's Triangle不同的是，本题第一行rowIndex为0，即行号从0开始，而前一题采用二维数组时是从1开始，所以第一个条件判断应根据Note that the row index starts from 0.小于0时为NULL；其次是，慎用a[j] += a[j - 1]出错，因为for循环时a[j-1]都会改变，使用赋值运算符时需要仔细。











