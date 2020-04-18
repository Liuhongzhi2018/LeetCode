#  整数中1出现的次数（从1到n整数中1出现的次数）


## 题目描述

求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

## 代码实现

1.遍历法
```python
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1,n+1):
            for s in str(i):
                if s == "1":
                    count += 1
        return count
```
运行时间：40ms

占用内存：5840k


2.逐位比较法
```python
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n<1:
            return 0
        count, base, round = 0,1,n
        while round>0: 
            weight = round%10
            round /= 10
            count += round*base
            if weight == 1:
                count += (n%base)+1
            if weight>1:
                count+=base
            base*=10
        return count
```
运行时间：21ms

占用内存：5860k


## 思路总结

1.  
对区间范围内的数字进行遍历。

2.    
考虑将n的十进制的每一位单独拿出讨论，每一位的值记为weight。  
1) 个位。从1到n，每增加1，weight就会加1，当weight加到9时，再加1又会回到0重新开始。那么weight从0-9的这种周期出现次数取决于n的高位；看weight值，weight大于1时，1又会出现1次。  
2）十位。对于10位来说，其0-9周期的出现次数与个位的统计方式是相同的。不同点在于：从1到n，每增加10，十位的weight才会增加1，所以，一轮0-9周期内，1会出现10次。即rount*10。 

对个位来说：  
若个位大于0，1出现的次数为round * 1+1
若个位等于0，1出现的次数为round * 1

对其它位来说，记每一位的权值为base，位值为weight，该位之前的数是former。  
若weight为0，则1出现次数为round * base
若weight为1，则1出现次数为round * base+former+1
若weight大于1，则1出现次数为rount * base+base
