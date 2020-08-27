# Convert a Number to Hexadecimal 

## 问题分析

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，通常使用补码运算方法。


## 代码实现

1.
``` C++
class Solution {
public:
    string toHex(int num) {
        int count=0;
        if(!num)  return "0";
        string hex;
        while(num&&count<8){
            int temp=num&15;
            if(temp<10) hex.push_back('0'+temp);
            else hex.push_back('a'+temp-10);
            num=num>>4;
            count++;
        }
        reverse(hex.begin(),hex.end());
        return hex;
    }
};
```

2.低位取余 + 倒转
```python
class Solution:
    def toHex(self, num: int) -> str:
        dic = '0123456789abcdef' 
        string = '' 
        if num == 0: 
            return '0' 
        elif num>0: 
            while num != 0: 
                string = dic[num%16] + string 
                num = num // 16 
            return string 
            
        else: num = -num-1 
        while num != 0: 
            string = dic[15-num%16] + string 
            num = num // 16 
        if len(string)<8: 
            string = (8-len(string))*'f'+string
        return string 
```

## 总结体会

本题要求将有符号的十进制转化为十六进制，需要解决的问题主要是补码运算和方向输出问题，需要注意的是本题要求十六进制中包含的是小写字母。

在算法设计上，首先声明一个字符串hex用于保存十六进制数；其次当满足8位十六进制数要求时，进入while循环，在hex中由高到低保存转换结果；最后将字符串反转，返回hex即为所求字符串。

低位取余 + 倒转方法：  
1.等于零时返回'0'  
2.正数正常采用余数定理  
3.负数取补码
