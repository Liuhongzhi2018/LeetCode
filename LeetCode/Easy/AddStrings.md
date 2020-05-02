# Add Strings

## 问题分析
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。


## 代码实现
``` C
char* addStrings(char* num1, char* num2) {
    int n1 = strlen(num1);
    int n2 = strlen(num2);
    int sum = n1 > n2 ? n1 + 1 : n2 + 1;
    
    char * sumStr = (char *)malloc((sum + 1) * sizeof(char));
    sumStr[sum] = '\0';
    
    char carryFlag = 0;
    int tmpNum = 0;
    int i;
    for (i = 1; i <= sum; i++) {
        tmpNum = carryFlag;
        if (i <= n1)  tmpNum += (num1[n1 - i] - '0');
        if (i <= n2)  tmpNum += (num2[n2 - i] - '0');
        
        if (tmpNum > 9) {
            tmpNum -= 10;
            carryFlag = 1;
        } else   carryFlag = 0;
        
        sumStr[sum - i] = tmpNum + '0';
    }
    
    if (sumStr[0] == '0')  sumStr++;
    return sumStr;
}
```

## 总结体会

本题要求两个字符串形式的整数之和，需要按照加法的计算法则，由低位向高位逐位相加。

在算法设计上，首先初始化需要保存到的字符串，将数字字符转换成相应的整型；其次用carryflag用来判断是否需要进位；最后将得到的和按照字符串sumstr格式返回。