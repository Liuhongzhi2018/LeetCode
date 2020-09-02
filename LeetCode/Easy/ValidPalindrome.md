#  Valid Palindrome

## 问题分析

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

## 代码实现

1.
``` C
bool isPalindrome(char* s) {
    int len = strlen(s);
    if (len == 0) return true;
    char *front = s;
    char *rear = s + len - 1;
    while (front < rear) {
        if(isalnum(*front)==0) {
            front++;
            continue;
        }
        if (isalnum(*rear)==0) {
            rear--;
            continue;
        }
        if (tolower(*front++) != tolower(*rear--)) return false;
    }
    return true;
}
```

2.双指针法
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        lp, rp = 0, n-1
        while lp < rp:
            while lp < rp and not s[lp].isalnum():
                lp += 1
            while lp < rp and not s[rp].isalnum():
                rp -= 1
            if lp < rp:
                if s[lp].lower() != s[rp].lower():
                    return False
                lp, rp = lp + 1, rp - 1
        return True
```

## 总结体会

本题要求验证回文字符串，采用类似队列的前端front和后端rear两个指针指向字符串的首尾元素，逐步向中心元素逼近，同时比较元素是否符合回文要求。

需要注意3点，一是按照题目要求，空字符串定义为有效回文串，返回true；二是学习使用isalnum的库函数，判断是否为字母或数字，若不是则为0；三是根据题目要求，不区分大小写，故学习使用tolower库函数统一转化为小写字母进行比较。

在原字符串 s 上使用双指针。在移动任意一个指针时，需要不断地向另一指针的方向移动，直到遇到一个字母或数字字符，或者两指针重合为止。也就是说，我们每次将指针移到下一个字母字符或数字字符，再判断这两个指针指向的字符是否相同。








