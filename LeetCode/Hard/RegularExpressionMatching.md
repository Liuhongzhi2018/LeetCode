#   Regular Expression Matching

## 问题分析

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 ' * ' 的正则表达式匹配。

## 代码实现

1. 动态规划
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        tmp = [[False]*(len(s)+1) for _ in range(len(p)+1)]
        tmp[0][0] = True
        for i in range(1, len(p)):
            tmp[i+1][0] = tmp[i-1][0] and p[i] == '*'
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    tmp[i+1][j+1] = tmp[i][j+1] or tmp[i-1][j+1]
                    if p[i-1]==s[j] or p[i-1]=='.':
                        tmp[i+1][j+1] |= tmp[i+1][j]
                else:
                    tmp[i+1][j+1] = tmp[i][j] and (p[i]==s[j] or p[i]=='.')
        return tmp[-1][-1]
```

2.暴力解
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1]=="*":
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])
```


## 思路总结

典型动态规划题