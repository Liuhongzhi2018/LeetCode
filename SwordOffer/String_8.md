# 扑克牌顺子


## 题目描述

LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。

## 代码实现

1. 遍历法
```python
# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers: 
                return False 
        numbers.sort() 
        zeroNums = 0
        for i in range(len(numbers) - 1): 
            if numbers[i] == 0: 
                zeroNums += 1 
            elif 0 < numbers[i + 1] - numbers[i] <= zeroNums + 1: 
                zeroNums -= (numbers[i+1] - numbers[i] -1) 
            else: 
                return False 
        return True
```
运行时间：27ms

占用内存：5868k

2.找满足条件
```python
# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        min, max, flag = 14, -1, 0 
        if len(numbers) != 5: 
                return False 
        for num in numbers: 
            if num == 0: 
                continue 
            if (flag>>num)&1 == 1: 
                return False
            #用二进制位来判断是否有数字重复 
            flag = flag | (1<<num) 
            if num > max: 
                max = num 
            if num < min: 
                min = num 
            if max - min >= 5: 
                return False 
        return True

```
运行时间：38ms

占用内存：5828k


## 思路总结

2：  
满足两个条件即可。  
1. 除0外没有重复的数  
2. max - min < 5  