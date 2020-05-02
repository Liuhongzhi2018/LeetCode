#  Longest Substring Without Repeating Characters

## 问题分析
Given a string, find the length of the longest substring without repeating characters.

给定一个字符串，找出不含有重复字符的最长子串的长度。

## 代码实现
``` C
int lengthOfLongestSubstring(char* s) {
    int len = 0;
    char *point = s;
    char *temp;
    char *add[128] = { 0 };
    while (*point) {
        temp = add[*point];
        add[*point] = point;
        if (temp >= s) {
            len = point - s > len ? point - s : len;
            s = temp + 1;
        }point++;
    }
    len= point -s>len? point - s : len;
    return len;
}
```

## 总结体会

本题要求根据给定的字符串，找出其中不含重复字符的最长子串。题目需要注意的是，要求找到的是子串，即连续不间断的字符元素，否则找出的子序列不满足要求；根据lengthOfLongestSubstring函数名，可知Expected Result是子串长度，而不是返回找出的子串。

在算法设计上，首先定义一个指针数组，保存字符串元素的地址；然后对字符串进行遍历，如果出现重复字符串，字符串指针s向后移动一位，直到遍历字符串所有元素；最后得到当前指针到头指针的步长，返回len即所求子串长度。

