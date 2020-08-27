#  Excel Sheet Column Title

## 问题分析

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

给定一个正整数，返回它在 Excel 表中相对应的列名称。

## 代码实现

1.
``` C
int number(int n)
{
    int count = 0;
    while (n) {
        n = (n - 1) / 26;
        count++;
    }
    return count;
}

char* convertToTitle(int n)
{
    if (n <= 0)   return NULL;
    int len = number(n);
    int temp, count = 0;
    char *column = (char *)malloc(sizeof(char)*len + 1);
    while (n) {
        temp = (n - 1) % 26;
        n = (n - 1) / 26;
        column[len - count - 1] = 'A' + temp;
        count++;
    }
    column[count] = '\0';
    return column;
}
```

2.
```python
class Solution:
    def convertToTitle(self, n: int) -> str:
        return "" if not n else self.convertToTitle(n//26-(0 if n%26 else 1))+" ABCDEFGHIJKLMNOPQRSTUVWXYZ"[n%26 if n%26 else 26]
```

## 总结体会

在日常使用的Excel表格中，行标号从1开始向下，列标号从A开始向右，本题要求的是给定第n列求出对应列标号。

首先，两个难点，一个是标号的字符串长度未知，另一个是列标号的字母排序未知。可以知道，第1列到第26列是1个字符，第27到702是2个字符，因此调用int number(int n)函数，返回需要动态内存分配的字符串长度，解决第一个难点。字母排序遵循二十六进制，算法设计上是从低位到高位，即从右至左依次确定字母，temp是字母表中距A的偏移量。

最后字符串末位补'\0'，返回column数组指针。











