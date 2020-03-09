# 表示数值的字符串


## 题目描述

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。


## 代码实现

1. 条件分析法
```python
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        sign, signe, signdot = 0, 0, 0
        numlist = [str(i) for i in range(10)]
        alphalist = [chr(i) for i in range(97,123)]+[chr(i) for i in range(65,91)]
        alphalist.remove('e')
        alphalist.remove('E')
        loc = 0
        # print(alphalist)
        for w in s:
            # print(w)
            if w == '+' or w == '-' and sign == 0:
                if loc == 0:
                    sign = 1
                    continue
                else:
                    return False
            if w == '+' or w == '-' and sign == 1:
                # print("error1")
                return False
            if w in alphalist:
                # print("error2")
                return False
            if w == '.' and signdot == 1:
                # print("error3")
                return False
            if w == '.' and signdot == 0:
                if signe == 0:
                    signdot = 1
                    continue
                else:
                    return False
            if w == 'e' or w == 'E' and signe == 0:
                # print("error4")
                signe = 1
                loc = 0
                sign = 0
                if w == 'e':
                    prel = s.split('e')
                    if len(prel[1]) == 0:
                        return False
                else:
                    potl = s.split('E')
                    if len(potl[1]) == 0:
                        return False
                continue
            if w == 'e' or w == 'E' and signe == 1:
                # print("error5")
                return False
            loc += 1
        return True
```
运行时间：22ms

占用内存：5836k

2. 特殊情况讨论法
```python
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        allowDot, allowE = True, True
        for i in range(len(s)):
            if s[i] in "+-" and (i == 0 or s[i-1] in "Ee") and i != len(s)-1:
                continue
            elif allowDot and s[i] == ".":
                allowDot = False
                if i == 0 or i == len(s) -1 or allowE == False:
                    return False
            elif allowE  and s[i] in "Ee":
                allowE = False
                if i == len(s)-1:
                    return False
            elif s[i] not in "0123456789":    # 最后验证是否出现了其他字符
                return False
        return True
```

运行时间：26ms

占用内存：5856k



## 思路总结

1. 条件分析法。对所给的测试用例的条件进行逐一判断。

2. 特殊情况讨论法。

在给出的可能出现的字符串中，有三个字符比较特殊，"±"，"e or E"，"."，需要对着几种情况进行考虑：

"±"只能出现在字符串首或者字符"e or E"后面，且不能出现在最后一位。
"."不能出现在字符串首，也不能出现在字符串尾部，也不能出现在字符"e or E"后面，且不能出现两次。
"e or E"不能出现两次且不能出现在字符串尾部。
除了0–9和上面三个字符，不能出现其他的字符。
在具体的实现过程中，由于"e or E"和"."不能出现两次，那么我们可以设置两个表示这两个字符能否在出现的标志。