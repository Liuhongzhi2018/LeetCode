#  First Unique Character in a String

## 问题分析
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

## 代码实现
``` C
int firstUniqChar(char* s) {
    int i,j,count;
    int len = strlen(s);
    if (!len)  return -1;
    for (i = 0; i < len; i++) {
        count = 0;
        if (s[i] != -1) {
            for (j = i + 1; j < len; j++) {
                if (s[j] == s[i]) {
                    s[j] = -1;
                    count++;
                }
            }
        }
        if (count)  s[i] = -1;
    }
    for (i = 0; i < len; i++) {
        if (s[i] != -1) return i;
    }
    return -1;
}
```

## 总结体会

本题要求从给定字符串中找出第一个不重复的字符，受埃拉托斯特尼筛法的启发，筛掉重复的字符，保留只出现一次的字符。

在算法设计上，首先判断所给字符串是否为空，若是返回-1；其次对字符串元素进行遍历，当前字符及其后若重复则均赋值-1；最后再次遍历字符串元素，查找第一个不是-1的元素，将下标返回，第一次OJ Accepted。

