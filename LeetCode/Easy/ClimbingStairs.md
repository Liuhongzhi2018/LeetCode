# Climbing Stairs  

## 问题分析

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

假设你正在爬楼梯。需要 n 步你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。


## 代码实现

1.
``` C
   int climbStairs(int n) {
    if (n < 0) return -1;
	if (n == 0) return 0;
	if (n == 1) return 1;
	if (n == 2)return 2;
	int * a = (int *)malloc(sizeof(int) * n);
	a[0] = 1;
	a[1] = 2;
	for (int i = 2; i < n; i++) {
		a[i] = a[i - 1] + a[i - 2];
	}
	return a[n - 1];
}

```

2.
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        p = q = 0
        i = r = 1
        while i<= n:
            p = q
            q = r
            r = p + q
            i += 1

        return r
```

3.动态规划
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] +dp[i-2]

        return dp[-1]
```

## 总结体会

本题可以理解为需要求出用1和2为加法元素，和是指定的数值的组合可能。

输入的和可能为负数、正数和零，当和大于2时，进入循环条件语句。由于每次只能加1或加2，那么求得n的方法从n-1得到的或者从n-2得到，可以得出a[n] =a[n-1] + a[n-2]递推公式，最后返回方法个数值。

动态规划思路和算法
用 f(x)f(x)f(x) 表示爬到第 xxx 级台阶的方案数，考虑最后一步可能跨了一级台阶，也可能跨了两级台阶，所以我们可以列出如下式子：
f(x)=f(x−1)+f(x−2)  
它意味着爬到第 x 级台阶的方案数是爬到第 x−1 级台阶的方案数和爬到第 x−2 级台阶的方案数的和。很好理解，因为每次只能爬 1 级或 2 级，所以 f(x)只能从 f(x−1) 和 f(x−2) 转移过来，而这里要统计方案总数，我们就需要对这两项的贡献求和。  
以上是动态规划的转移方程，下面我们来讨论边界条件。我们是从第 0 级开始爬的，所以从第 0 级爬到第 0 级我们可以看作只有一种方案，即 f(0)=1；从第 0 级到第 1 级也只有一种方案，即爬一级，f(1)=1。这两个作为边界条件就可以继续向后推导出第 n 级的正确结果。我们不妨写几项来验证一下，根据转移方程得到 f(2)=2，f(3)=3，f(4)=5......我们把这些情况都枚举出来，发现计算的结果是正确的。  
我们不难通过转移方程和边界条件给出一个时间复杂度和空间复杂度都是 O(n) 的实现，但是由于这里的 f(x) 只和 f(x−1) 与 f(x−2) 有关，所以我们可以用「滚动数组思想」把空间复杂度优化成 O(1)。
