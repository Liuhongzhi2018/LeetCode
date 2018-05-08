#  Valid Palindrome

## 问题分析
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

## 代码实现
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

## 总结体会

本题要求验证回文字符串，采用类似队列的前端front和后端rear两个指针指向字符串的首尾元素，逐步向中心元素逼近，同时比较元素是否符合回文要求。

需要注意3点，一是按照题目要求，空字符串定义为有效回文串，返回true；二是学习使用isalnum的库函数，判断是否为字母或数字，若不是则为0；三是根据题目要求，不区分大小写，故学习使用tolower库函数统一转化为小写字母进行比较。











