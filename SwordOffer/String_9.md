# 把字符串转换成整数


## 题目描述


将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0

## 代码实现

1. 遍历法
```python
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        length = len(s)
        if length == 0:
            return 0
        #确定符号
        sign = 1#正负符号
        flag = 1#标志位，看s[0]是除数字0-9外的正负号还是字母，是正负号的时候为0，字母时为1
        if s[0] == '-':
            flag = 0
            sign = -1
            #s[0] = '0' #python中字符串是不可变对象，不能用下标赋值的方式去改变字符串 
        elif s[0] == '+':
            flag = 0
            sign = 1
            #s[0] = '0'
        #遍历字符串，进行转换    
        num = 0#最后返回的数字
        for i in range(length):
            #是数字时进行类型转换
            if s[i]>='0' and s[i]<='9':
                num = num*10 + (ord(s[i]) - ord('0'))#ord()函数得到其ascill
                #num = num*10 +int(s[i])#也可以直接用int()函数转换
            #除数字外判断是正负号还是字母，如果是正负号，从下一位开始；是字母则认为非法的数值表达，返回0
            else:
                if flag == 0:
                    continue
                else:
                    num = 0
                    break
        return num * sign
```
运行时间：25ms

占用内存：5732k

2. 直接转换法
```python
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        sum = 0
        temp = 0
        negaFlag = 1#符号
        for ss in s:
            if ss == "0":
                temp = 0
            elif ss == "1":
                temp = 1
            elif ss == "2":
                temp = 2
            elif ss == "3":
                temp = 3
            elif ss == "4":
                temp = 4
            elif ss == "5":
                temp = 5
            elif ss == "6":
                temp = 6
            elif ss == "7":
                temp = 7
            elif ss == "8":
                temp = 8
            elif ss == "9":
                temp = 9
            elif ss == "-":
                negaFlag = -1
            elif ss == "+":
                negaFlag = 1
            else:
            #除0-9的数字和正负号外的字母的情况
                return 0
            sum += temp
            sum *= 10
        return negaFlag * sum / 10 
        #以+2456为例，最后得到的是24560,所以最后需要除以10
```
运行时间：23ms

占用内存：5860k




## 思路总结

