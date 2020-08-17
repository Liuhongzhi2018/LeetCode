#  Different  Ways to Add Parentheses

## 问题描述

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

## 代码实现

1.
``` python
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if '+' not in input and '-' not in input and '*' not in input:
            return [int(input)]
        ans = []
        for i in range(len(input)):
            if input[i] in ['+','-','*']:
                part1 = self.diffWaysToCompute(input[:i])
                part2 = self.diffWaysToCompute(input[i+1:])
                for p in part1:
                    for q in part2:
                        if input[i] == '+':
                            ans.append(p+q)
                        elif input[i] == '-':
                            ans.append(p-q)
                        else:
                            ans.append(p*q)
        return ans
```


## 思考总结

分解原问题：每个运算符将表达式分成左右两个子问题  
解决子问题：表达式只有数字时，返回数字  
合并(回溯，即退栈)：左右子问题结果两两组合  
函数diffWaysToCompute用于计算表达式所有可能的结果，输入一个字符串，返回的是一个list。
