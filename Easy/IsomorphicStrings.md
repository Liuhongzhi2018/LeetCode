#  Isomorphic Strings

## 问题分析
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Note: You may assume both s and t have the same length.

给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

说明: 你可以假设 s 和 t 具有相同的长度。


## 代码实现
``` C
bool isIsomorphic(char* s, char* t)
{
    if ((s==NULL&&t!=NULL)||(s!= NULL&&t== NULL))
        return false;
    int len1 = strlen(s);
    int len2 = strlen(t);
    if (len1 != len2) return false;
    int sTt[256];
    int tTs[256];
    int i = 0;
    for (i = 0; i<256; i++) {
        sTt[i] = -1;
        tTs[i] = -1;
    }
    for (i = 0; i<len1; i++) {
        if (sTt[s[i]] == -1) {
            if (tTs[t[i]] == -1) {
                sTt[s[i]] = t[i]; 
                tTs[t[i]] = s[i]; 
            }
            else return false;
        }
        else if (sTt[s[i]] != t[i])  return false;
    }
    return true;
}
```

## 总结体会

本题要求判断字符串是否同构，可以理解为s字符串的某一个字符，可以映射到t字符串的相应字符并保持彼此之间的映射关系。

如果字符串满足同构的关系，那么字符串间长度一定相等且空或非空一致； 其次用数组保存字符串元素，遍历数组元素，判断是否存在映射关系。