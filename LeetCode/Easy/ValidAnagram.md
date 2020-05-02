#  Valid Anagram

## 问题分析
Given two strings s and t , write a function to determine if t is an anagram of s.

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

## 代码实现
``` C
bool isAnagram(char* s, char* t) {
    int slen = strlen(s);
    int tlen = strlen(t);
    int i;
    int a[26] = { 0 };
    if (s == NULL&&t == NULL) return true;
    if (slen != tlen)  return false;
    for (i = 0; i < slen; i++) {
        a[s[i] - 'a']++;
        a[t[i] - 'a']--;
    }
    for (i = 0; i < 26; i++) {
        if (a[i])  return false;
    }
    return true;
}
```

## 总结体会

本题考察两个字符串是否为异位词，可以理解为两个字符串字母组成相同，不能有一个字符串出现另一个字符串没有的单词。

在算法设计上，首先判断两个字符串长度是否相等，如果不相等一定不是异位词。其次，定义一个长度为26的整型数组，元素均为0，对应英文中的26个小写字母a-z。然后由遍历字符串s和t，s中出现某一字母则在数组对应的位置上数值加1，t中出现相同字母则对应位置减1。如果在s和t中所有字符循环完毕后，整型数组a中的所有元素都为0，可认为标志位均为0，则认为s 与 t 的是字母异位词。