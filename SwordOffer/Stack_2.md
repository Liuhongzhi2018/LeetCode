# 包含min函数的栈


## 题目描述

定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。

## 代码实现

1. 用新栈保存最小值
```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minL = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minL != []:
            if node < self.minL[-1]:
                self.minL.append(node)
            else:
                self.minL.append(self.minL[-1])
        else:
            self.minL.append(node)
    def pop(self):
        # write code here
        if self.stack == []:
            return None
        self.minL.pop()
        return self.stack.pop()
    def top(self):
        # write code here
        if self.stack == []:
            return None
        return self.stack[-1]
    def min(self):
        # write code here
        if self.minL == []:
            return None
        return self.minL[-1]
```
运行时间：28ms

占用内存：5868k



## 思路总结

在满足要求的时间复杂度条件，应该用新栈存储最小值，元素数量与Stack相同。