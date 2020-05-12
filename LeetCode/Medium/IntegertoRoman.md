#  Integer to Roman

## 问题分析
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four.

罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

通常情况下，罗马数字中小的数字在大的数字的右边。但例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。


## 代码实现
1.
``` C
int Position(char* roman,int num,char pre,char mid,char lat){
    switch(num){
        case 1:roman[0]=pre;return 1;
        case 2:roman[0]=pre;roman[1]=pre;return 2;
        case 3:roman[0]=pre;roman[1]=pre;roman[2]=pre;return 3;
        case 4:roman[0]=pre;roman[1]=mid;return 2;
        case 5:roman[0]=mid;return 1;
        case 6:roman[0]=mid;roman[1]=pre;return 2;
        case 7:roman[0]=mid;roman[1]=pre;roman[2]=pre;return 3;
        case 8:roman[0]=mid;roman[1]=pre;roman[2]=pre;roman[3]=pre;return 4;
        case 9:roman[0]=pre;roman[1]=lat;return 2;
    }
    return 0;
}
char* intToRoman(int num) {
    char* roman=(char*)malloc(sizeof(char)*16);
    int cnt=0;
    if(num/1000!=0){
        cnt+=Position(roman+cnt,num/1000,'M','#','#');
        num%=1000;
    }
    if(num/100!=0){
        cnt+=Position(roman+cnt,num/100,'C','D','M');
        num%=100;
    }
    if(num/10!=0){
        cnt+=Position(roman+cnt,num/10,'X','L','C');
        num%=10;
    }
    if(num!=0){
        cnt+=Position(roman+cnt,num,'I','V','X');
    }
    roman[cnt]='\0';
    return roman;
}
```

2.字典法
```python
class Solution:
    def intToRoman(self, num: int) -> str:
        Rdict = {
            1000:"M",
            900:"CM",
            500:"D",
            400:"CD",
            100:"C",
            90:"XC",
            50:"L",
            40:"XL",
            10:"X",
            9:"IX",
            5:"V",
            4:"IV",
            1:"I"
        }
        res = ""
        for i in Rdict:
            count = num // i
            if count:
                res += count*Rdict[i]
                num %= i
        return res
```

3.
```python
class Solution:
    def intToRoman(self, num: int) -> str:
        ref = {
            "M":1000,
            "CM":900,
            "D":500,
            "CD":400,
            "C":100,
            "XC":90,
            "L":50,
            "XL":40,
            "X":10,
            "IX":9,
            "V":5,
            "IV":4,
            "I":1
        }
        sorted_ref = sorted(ref.keys(),key=ref.get, reverse=True)
        res = ""
        for i in sorted_ref:
            while num >= ref[i]:
                res += i
                num -= ref[i]
        return res
```

## 总结体会

本题要求将所给整数转换为罗马数字输出，需要理解清楚转换原则、各字母代表的含义以及可能存在的位置。

在算法设计上，首先在intToRoman函数中判断整数由千位到个位的各位数字；其次Position函数中采用穷举法和switch-case条件语句，确定10以内罗马字母的排列位置，整数的每一位最多由三个罗马字母组成；最后字符串最后一位补零，返回即为所求。



