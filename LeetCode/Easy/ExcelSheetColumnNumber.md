#  Excel Sheet Column Number

## 问题分析
Given a column title as appear in an Excel sheet, return its corresponding column number.

给定一个Excel表格中的列名称，返回其相应的列序号。

## 代码实现
``` C
int titleToNumber(char* s) {  
    int num = 0;  
    char* p = s;
    while(*p!=NULL){
        num = num*26 + *p-'A'+1;
        p++;
    } 
    return num;  
}  
```

## 总结体会

本题要求Excel表格中的列对应的序号，与之前ExcelSheetColumnTitle题目类似，不同的是将字母转成数字形式。

本题的算法设计思路与ExcelSheetColumnTitle题目正好相反。首先，遍历字符串，将对应的字母转成二十六进制数字，需要注意这种二十六进制中A对应的是1，而Z对应的是26；其次在循环中，采用加权的思路进行叠加和进制转换；最后返回对应序号。












