#   Longest Valid Parentheses

## 问题分析

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。


## 代码实现


1.
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stk = [-1]
        for i, c in enumerate(s):
            if c == "(":
                stk.append(i)
            elif len(stk)==1:
                stk.pop()
                stk.append(i)
            else:
                stk.pop()
                res = max(res,i-stk[-1])
        return res
```


## 思路总结

本题需要用到括号stack，显然只有遇到左括号"("的时候，append到stack中，遇到右括号")"时则pop出。

难点在于：如何记录当前的有效长度？

因为我们知道遇到"("时会append，所以应该在下标上做文章。

首先初始化res和stack，然后遍历所有的下标及其元素，进行分情况讨论。