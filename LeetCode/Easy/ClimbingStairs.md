# Climbing Stairs  

## 问题分析
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

假设你正在爬楼梯。需要 n 步你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。


## 代码实现
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

## 总结体会
本题可以理解为需要求出用1和2为加法元素，和是指定的数值的组合可能。

输入的和可能为负数、正数和零，当和大于2时，进入循环条件语句。由于每次只能加1或加2，那么求得n的方法从n-1得到的或者从n-2得到，可以得出a[n] =a[n-1] + a[n-2]递推公式，最后返回方法个数值。
