# Sqrt(x)  

## 问题分析

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

## 代码实现

1.
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

2.袖珍计算器算法
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: 
            return 0 
        ans = int(math.exp(0.5 * math.log(x))) 
        return ans + 1 if (ans + 1) ** 2 <= x else ans
```

3.二分查找
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, res = 0, x, -1
        while l <= r:
            mid = (l + r ) // 2
            if mid * mid <= x:
                res = mid
                l = mid + 1
            else :
                r = mid - 1
        return ans
```

4.牛顿迭代
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi
        return int(x0)
```

## 总结体会

[https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/](https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/)

袖珍计算器算法，是一种用指数函数 exp⁡ 和对数函数 ln⁡ 代替平方根函数的方法。我们通过有限的可以使用的数学函数，得到我们想要计算的结果。

二分查找法，由于 xxx 平方根的整数部分 ans\textit{ans}ans 是满足 k2≤xk^2 \leq xk2≤x 的最大 kkk 值，因此我们可以对 kkk 进行二分查找，从而得到答案。二分查找的下界为 0，上界可以粗略地设定为 x。在二分查找的每一步中，我们只需要比较中间元素 mid 的平方与 x 的大小关系，并通过比较的结果调整上下界的范围。由于我们所有的运算都是整数运算，不会存在误差，因此在得到最终的答案 ans 后，也就不需要再去尝试 ans+1 了。

牛顿迭代法是一种可以用来快速求解函数零点的方法。为了叙述方便，我们用 C 表示待求出平方根的那个整数。显然，C 的平方根就是函数
y = f(x) = x * x − C 的零点。

牛顿迭代法的本质是借助泰勒级数，从初始值开始快速向零点逼近。我们任取一个 x0 作为初始值，在每一步的迭代中，我们找到函数图像上的点 (xi,f(xi))，过该点作一条斜率为该点导数 f′(xi)的直线，与横轴的交点记为 xi+1。xi+1相较于 xi 而言距离零点更近。在经过多次迭代后，我们就可以得到一个距离零点非常接近的交点。下图给出了从 x0 开始迭代两次，得到 x1 和 x2 的过程。