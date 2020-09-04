#  Longest Repeating Character Replacement

## 问题描述

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 10^4.

给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意:
字符串长度 和 k 不会超过 10^4。


## 代码实现

1.双指针滑动窗
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slen = len(s)
        if k > slen:
            return slen
        s_dict = collections.defaultdict(int)
        max_val, ret = 0, 0
        lp = 0
        for rp in range(slen):
            s_dict[s[rp]] += 1
            max_val = max(max_val, s_dict[s[rp]])
            while rp - lp + 1 - max_val > k:
                s_dict[s[lp]] -= 1
                lp += 1
            ret = max(ret, rp - lp + 1)
        return ret
```


## 思路总结

用字典s_dict来存储滑动窗口中所有字母出现的次数；  
用变量max_val来存储字典中出现次数最多的字母的出现次数；  
然后移动和调整窗口。

没向右移动一次，便会有一个字母的出现次数发生变化，而这个变化才有可能使max_val改变；  
窗口的大小为right - left + 1，那么right - left + 1 - max_val便是需要替换的字母数量，那么为什么要用max_val呢，因为这样可以使替换的数量降到最低；  
若right - left + 1 - max_val > k，则说明这个窗口已经无法替换做到题目要求了，需要移动窗口的左边界。