#  Longest Substring Without Repeating Characters

## 问题分析

Given a string, find the length of the longest substring without repeating characters.

给定一个字符串，找出不含有重复字符的最长子串的长度。

## 代码实现

1.
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

2.
```python 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, res, cache = 0, 0, {}
        for idx, c in enumerate(s):
            if c in cache and cache[c] >= start:
                start = cache[c] + 1
                cache[c] = idx

            else:
                cache[c] = idx
                cur = idx - start + 1
                res = max(res, cur)

        return res
```



## 总结体会

本题要求根据给定的字符串，找出其中不含重复字符的最长子串。题目需要注意的是，要求找到的是子串，即连续不间断的字符元素，否则找出的子序列不满足要求；根据lengthOfLongestSubstring函数名，可知Expected Result是子串长度，而不是返回找出的子串。

在算法设计上，首先定义一个指针数组，保存字符串元素的地址；然后对字符串进行遍历，如果出现重复字符串，字符串指针s向后移动一位，直到遍历字符串所有元素；最后得到当前指针到头指针的步长，返回len即所求子串长度。

首先res用于存储最长字串长度，start开始下标，cache每个字母最近的下标，遍历字符串的字符和下标，判断是否在cache中见过该字符；  
如果不存在，更新当前字符串以及res，如果存在判断下标是否在start之后；  
如果下标在start之后，更新start以及当前字符串和res。  
时间复杂度：O(N)，其中 N 是字符串的长度。