#  Unique Paths

## 问题分析

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

## 代码实现

1.
``` C++
class Solution {
public:
    int uniquePaths(int m, int n) {
    if(m<=0||n<=0) return 0;
    int i;
    long long res=1;
    for(i=n;i<m+n-1;i++){
        res=res*i/(i-n+1);
     }
    return (int)res;
    }
};
```

2.动态规划
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        for i in range(1, m): 
            for j in range(1, n): 
                dp[i][j] = dp[i-1][j] + dp[i][j-1] 
        return dp[-1][-1]
```

3.排列组合
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
```

## 总结体会

本题要求机器人所在网格位置，求出到指定网格右下角的路径数量。

在算法设计上，首先判断机器人所在位置是否在网格中，即m和n是否均大于0，否则返回；在求路径个数时，运用数学计算，从(m-1)位置到(m+n-2)和从(n-1)到(m+n-2)步数相同均为(m+n-2)!/[(m-1)!*(n-1)!]；最后返回res即为所求路径数。
