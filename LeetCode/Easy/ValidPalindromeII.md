#  Valid Palindrome II

## 问题分析

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome. 

给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

## 代码实现

1.
``` python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        re = s[::-1]
        if re == s:
            return True
        left,right=0,len(s)-1
        while left < right:
            if s[left] != s[right]:
                return s[left+1:right+1] == s[left+1:right+1][::-1] or s[left:right] == s[left:right][::-1]
            left += 1
            right -= 1
        return True
```

## 总结体会

本题的关键是处理删除一个字符。在使用双指针遍历字符串时，如果出现两个指针指向的字符不相等的情况，我们就试着删除一个字符，再判断删除完之后的字符串是否是回文字符串。

如果首尾元素相等，则左右指针同时向中间移动一个位置；如果不相等时，判断删除左指针元素后是否为回文字符串，或者删除右指针后是否为回文字符串。
