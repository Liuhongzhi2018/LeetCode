#  Word Pattern

## 问题分析
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Notes: You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

给定一种 pattern(模式) 和一个字符串 str，判断 str 是否遵循相同的模式。

这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。

说明: 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。

## 代码实现
``` C
bool wordPattern(char* pattern, char* str) {
    int i, j, len = strlen(pattern);
    if (len == 0)  return false;
    int st[len];
    char *cut, *saveptr, temp[strlen(str)];
    //for (i = 0; i < len; i++)  search[i] = -1;
    memset(st, -1, sizeof(st));
    strcpy(temp, str);
    cut = strtok_r(temp, " ", &saveptr);
    
    for (i = 0; i < len; i++) {
        int a = strchr(pattern, pattern[i]) - pattern;

        if (cut == NULL) break;
        int b = strstr(str, cut) - str;

        for (j = 0; j < a; j++)
            if (st[j] == b) return false;

        if (st[a] == -1)  st[a] = b;
        else if (st[a] != b)  return false;

        cut = strtok_r(NULL, " ", &saveptr);
    }
    if ((cut == NULL) ^ (i == len))  return false;
    return true;
}
```

## 总结体会

本题要求判断所给的字符串是否符合给定的pattern模式，各单词字母的模式以及由空格和单词组成的字符串整体的模式均应符合所给模式。

在算法设计上，使用memset函数，将数组各元素赋值为-1；使用strtok_r函数将临时字符串temp以空格为标志进行切分，用于进行字符串str整体模式判断；使用strchr函数查找pattern元素在pattern字符串首次出现的位置；使用strstr函数判断cut字符串是否为str字符串的子串。通过将各单词内与pattern比较，再将字符串各单词组成模式与pattern比较，从而判断字符串是否符合所给pattern模式。

值得注意的是，用len变量初始化st数组之前，需要判断len是否为0，否则报错variable length array bound evaluates to non-positive value 0，应该在初始化前先判断，若为非0则可以初始化st数组。

