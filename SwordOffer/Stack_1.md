# 用两个栈实现队列 


## 题目描述

用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。


## 代码实现

1. 双栈倒序取出
```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.aStack = []
        self.oStack = []
    def push(self, node):
        # write code here
        self.aStack.append(node)
        
    def pop(self):
        # return xx
        if self.oStack == []:
            while self.aStack:
                self.oStack.append(self.aStack.pop())
        if self.oStack != []:
            return self.oStack.pop()
        else:
            return None
```

运行时间：43ms

占用内存：5624k


## 思路总结

首先栈结构是LIFO，队列结构是FIF。

用列表来保存队列元素时，插入元素操作是通过列表追加元素。但是删除元素时，需要将存储栈内的元素先取出，然后取栈顶元素。因此在pop时，先依次将存储栈内的元素弹出压入弹出栈中，此时在存储栈先入栈的元素在弹出栈是栈顶，此时再取出弹出栈的栈顶元素，即为先入队列的元素。