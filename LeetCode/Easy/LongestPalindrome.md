# Longest Palindrome

## 问题分析
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

## 代码实现
``` C
int longestPalindrome(char* s){
    int n = strlen(s);
    int letter[52] = {0};
    int i,len = 0;
    bool sign = false;
        for (i = 0; i < n; i++) {
            if (s[i] >= 'a' && s[i] <= 'z')  letter[s[i] - 'a']++;
            else  letter[s[i] - 'A' + 26]++;
        }
        for (i = 0; i < 52; i++) {
            if (letter[i] % 2 == 0)   len += letter[i];
            else {
                sign = true;
                len += letter[i] - 1;
            }
        }
        return sign ? len + 1 : len;
}
```

## 总结体会
本题要求根据所给的字符串，判断可以组成的最长回文串。需要注意的是，本题并不是在原有字符串上判断回文串最大长度，而是从所给字符串中找出可以组成回文串的字母，组成新的最长字符串，开始编译错误在于没有理解题目要求。

在算法设计上，首先定义一个整型数组用于保存大小写字母各自出现的次数，定义一个布尔变量判断是否出现的次数是否为奇数；其次遍历所给字符串，将各字母出现的次数记录下来，其中出现偶数次一定可以组成回文串，若出现大于1的奇数次可以记进字符串的统计中，同时对标志位进行修改；最后根据标志位的情况，返回回文串长度。