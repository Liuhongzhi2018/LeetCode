#   Substring with Concatenation of All Words

## 问题分析

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

## 代码实现


1.
```python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []
        unilen = len(words[0])
        res, sets = [], {}
        for word in words:
            sets[word] = sets.setdefault(word,0)+1
        for i in range(unilen):
            count, start, match_set = len(words),i,{}
            for j in range(i,len(s),unilen):
                substr = s[j:j+unilen]
                if substr in sets:
                    match_set[substr] = match_set.setdefault(substr,0)+1
                    count -= 1
                    while (match_set[substr]>sets[substr]):
                        remove = s[start:start+unilen]
                        start += unilen
                        match_set[remove] -= 1
                        count += 1
                    if count == 0:
                        res.append(start)
                else:
                    count, start, match_set = len(words),j+unilen,{}
        return res
```


## 思路总结

首先思路是将s划分成与words相同长度的word，然后进行匹配。  
用unilen存储单个单词的长度，大循环是从0，1，2开始分割单词。首先从下标为0开始分割单词，继续向前遍历3个3个的单词，如果没有匹配则不进行任何操作；从1开始，如果匹配则保存到cache中，start保存当前下标。