#  ZigZag Conversion

## 问题分析
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows。And then read line by line。

将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数，之后从左往右，逐行读取字符，"PAHNAPLSIIGYIR"实现一个将字符串进行指定行数变换的函数。

## 代码实现
``` C
char* convert(char* s, int numRows) {
    int i,j,k=0;
    int len=strlen(s);
    char* str;
    int l,l1;
    str=(char*)malloc((len+1)*sizeof(char));
    str[len]='\0';
    if(numRows==1)   l=1; 
    else    l=(numRows-1)*2;
    for(i=0;i<numRows;i++){
        j=i;   
        if(i==0 || i==numRows-1){       
            while(j<len) {       
               str[k]=s[j];
               k++;
               j+=l;
            }
        }
        else{
            l1=i*2;
            while(j<len){
                str[k]=s[j];
                k++;
                l1=l-l1;
                j+=l1;
            }
        }
    }
    return str;
}
```

## 总结体会

本题要求将所给字符串进行Z字形排列，需要注意的是Z的书写方式是竖向而不是横向，因此需要先将字符串从上到下排列再横向返回字符串。

在算法设计上，首先变量l保存间隔，numRows只有一行时两个数的间隔是1；其次第0行和第numRows-1行两个数的时间间隔是(m-1)\*2，中间行两个数的间隔是(m-1)\*2-i\*2和i\*2交替；最后用str字符串横向读取排列后的字符串，返回str即为所求。



