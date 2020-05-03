#  Longest Palindromic Substring

## 问题分析
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

## 代码实现

1.
``` C
int getlen(char *s, int a, int b, int len);
char* longestPalindrome(char* s);

int getlen(char *s, int a, int b, int len){
    int max = 0;
    for (; a>=0&&b<len; a--,b++){
        if (s[a] == s[b])  max+=2;
        else  break;
    }
    return max;
}

char* longestPalindrome(char* s)
{
    int len = strlen(s);
    int i,cur=0,temp,maxlen=1,index,maxindex=0;
    char *longeststr = NULL;

    if (len == 1)  return s;
    if (len==2 && s[0] == s[1])  return s;

    for (i=1; i<len-1; i++){
        if (s[i-1] == s[i]){
        cur = getlen(s, i-1, i, len);
            if (s[i] == s[i+1]){
                int temp = 1+getlen(s, i-1, i+1, len);
                cur = temp>cur?temp:cur;
            }
            index = i-(cur/2);
        }
        else if(s[i] == s[i+1]){
            cur = getlen(s, i, i+1, len);
            index = i-(cur/2)+1;
        }
        else if (s[i-1] == s[i+1]){
           cur = 1 + getlen(s, i-1, i+1, len);
           index = i-(cur/2);
        }

        if (cur > maxlen){
            maxlen = cur;
            maxindex = index;
        }
    }
    if (maxlen > 0){
        longeststr = (char *)calloc(maxlen+1, 1);
        memcpy(longeststr, s+maxindex, maxlen);
    }
    return longeststr;
}
```

2.
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            start = max(0, i-len(res)-1)
            temp = s[start : i+1]
            if temp == temp[::-1]:
                res = temp
            else:
                temp = temp[1:]
                if temp == temp[::-1]:
                    res = temp
        return res
```

## 总结体会

本题要求从字符串s中找到最长回文子串，即掌握回文字符的判断方法，返回字符串。

在算法设计上，主要考虑回文的特性是由中间的字母往两边扩散是对应相等的，由此检索所有的回文长度，记录最长的长度和起始位置，字符串检测结束后，再分配相应空间复制，返回字符串指针即为所求字符串。

回文字符串str==str[::-1]  
回文字符串性质，如果是回文字符串，那么去头去尾字符串str[1:-1]也为回文字符串。  
截取start到i的字符串，str[start:i+1]