#  Valid Perfect Square

## 问题分析

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

注意：不要使用任何内置的库函数，如 sqrt。

## 代码实现

1.
``` C
bool isPerfectSquare(int num) {
    int i;
    if (num< 1)  return false;
    if (num == 1) return true;
    for (i = 1; i <= num / 2; i++) {
        if (i * i == num)
            return true;
    }
    return false;
}
```

2.
```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2: 
            return True 
        left, right = 2, num // 2 
        while left <= right: 
            x = left + (right - left) // 2
            guess_squared = x * x 
            if guess_squared == num: 
                return True 
            if guess_squared > num: 
                right = x - 1 
            else: left = x + 1 
        return False
```


## 总结体会

本题要求判断所给正整数是否为完全平方数，即是否可以找到一个数的平方是所给整数。

算法设计上，采用for循环，从1开始进行遍历判断直到所给整数的一半，每次进行平方后与所给整数比较，如果找到符合条件的整数，返回true，否则false。

平方根相关问题通常可以在对数时间内求解。这里列出了从最坏到最好的三种标准对数时间的方法：
递归  
二分查找  
牛顿迭代法  
这些解决方法都有相同的起点。num 是一个有效的完全平方数若 x∗x==numx。