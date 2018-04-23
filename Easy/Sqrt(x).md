# Sqrt(x)  

## 问题分析
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。


## 代码实现
``` C
int mySqrt(int x) {
	if (x < 0) return -1;
	if (x == 0) return 0;
	double pre = 0;
	double next = 1;
	while ((next - pre) > 0.000001 || (next - pre) < -0.000001)
	{
		pre = next;
		next = (next + x / next) / 2.0;
	}
	return (int)(next);
}
```

## 总结体会
本题一开始采用顺序查找，结果未通过原因是出现溢出，当乘积超过int所表示范围后影响条件判断，输出结果错误。后采用牛顿切线法，将起始值设为1，然后迭代方式求出下一个切点对应横坐标值，若两个坐标值无限接近，即认为是所求的开平方值。
