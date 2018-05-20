#  Number of 1 Bits

## 问题分析
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。


## 代码实现
``` C
void convers(uint32_t n, char *s) {
    int i = 0;
    while (n!= 0){
        s[i] = (n % 2)+'0';
        i++;
        n = n / 2;
    }
    s[i] = '\0';
}
int hammingWeight(uint32_t n) {
    char s[33];
    memset(s, 0, sizeof(s));
    convers(n, s);
    int num = 0;
    for (int i = 0; i<32; i++)
        if (s[i] == '1') num++;
    return num;
}
```

## 总结体会

本题要求十进制无符号整数转换为二进制数时非零字符数，即汉明重量。需要了解的是汉明重量是字符串相对于同样长度的零字符串的汉明距离。从计算方法来讲，一个字符串的汉明重量，就是字符串中非零元素的个数。对于常用的二进制字符串，就是字符串中数字1的个数。

本题算法设计上分两个步骤。第一个是，十进制转换为二进制数，用convers函数保存为字符串；第二个步骤是，遍历字符串元素找出非零即1的元素个数，保存在num变量中，最后返回num值即为所求。