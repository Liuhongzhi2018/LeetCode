#  String to Integer (atoi)

## 问题分析
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

实现 atoi，将字符串转为整数。

在找到第一个非空字符之前，需要移除掉字符串中的空格字符。如果第一个非空字符是正号或负号，选取该符号，并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。

当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。

若函数不能执行有效的转换，返回 0。

## 代码实现
``` C
int myAtoi(char* str) {
    int sign=1,num=0,dec;
    while(*str==' ')  str++;
    if(*str=='-'){
        sign=-1;
        str++;
    }
    else if(*str=='+')   str++;
    while(*str){
        if(*str<'0' || *str>'9')  return sign*num;
        dec=*str-'0';
        if(sign==1 && num*10.0+dec>INT_MAX)   return INT_MAX;
        else if(sign==-1 && -num*10.0-dec<INT_MIN)   return INT_MIN;
        num= num*10+dec;
        str++;
    }
    return sign*num;
}
```

## 总结体会

本题要求将字符串转换为整数，即取出有效字符组成十进制整数。

在算法设计上，首先找到第一个有效正或者负符号位，保存在sign变量中；其次取出数字位组成整数，并且判断是否满足边界条件；最后将符号和无符号位相乘得到整数返回。

