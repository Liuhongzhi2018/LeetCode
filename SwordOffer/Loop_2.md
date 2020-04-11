#  跳台阶 


## 题目描述

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

## 代码实现

1. 循环法
```python
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number < 1:
            return 0
        if number == 1 or number == 2:
            return number
        count = 0
        n_1, n_2 = 1, 2
        for i in range(3, number+1):
            count = n_1 + n_2
            n_1,n_2 = n_2, count
        return count
```
运行时间：40ms

占用内存：5836k



## 思路总结

可以看成是裴波那契数列的应用，当n大于2时，第一步可以是1个也可以是2个，看成是2种不同的情况。