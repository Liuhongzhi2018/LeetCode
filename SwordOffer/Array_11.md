# 字符串的排列


## 题目描述

输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

## 代码实现

1. 
```python
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        ls = []
        lenss = len(ss)
        if lenss < 2:
            return ss
        for i in range(lenss):
            for j in map(lambda x: ss[i]+x, self.Permutation(ss[:i]+ss[i+1:])):
                if j not in ls:
                    ls.append(j)
        return ls
```
运行时间：43ms

占用内存：5724k





## 思路总结

化繁为简，我们怎样找到这道题的通式呢？像青蛙跳台阶的思想那样，无论输入的字符串有多长，其排列出来的组合式样式均可分为“第一个字符串+剩下的字符串”的样式，可以通过遍历赋予第一位上不同的字符。那剩下的字符串又可以如上分解。

这里有一点要注意，ss的索引字符串会超出范围，不过python在对字符串做切片操作时，当索引位置超出长度，python不会报错只会跳出本次循环。

当然我们还要考虑字符串中是否包含重复元素，因为在输入中有重复值时就会生产相同的字符串，因此在代码中加一个判断即可。
