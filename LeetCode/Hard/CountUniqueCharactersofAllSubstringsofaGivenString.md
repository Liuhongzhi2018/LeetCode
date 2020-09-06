#   Count Unique Characters of All Substrings of a Given String

## 问题描述

Let's define a function countUniqueChars(s) that returns the number of unique characters on s, for example if s = "LEETCODE" then "L", "T","C","O","D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.

On this problem given a string s we need to return the sum of countUniqueChars(t) where t is a substring of s. Notice that some substrings can be repeated so on this case you have to count the repeated ones too.

Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.

我们定义了一个函数 countUniqueChars(s) 来统计字符串 s 中的唯一字符，并返回唯一字符的个数。

例如：s = "LEETCODE" ，则其中 "L", "T","C","O","D" 都是唯一字符，因为它们只出现一次，所以 countUniqueChars(s) = 5 。

本题将会给你一个字符串 s ，我们需要返回 countUniqueChars(t) 的总和，其中 t 是 s 的子字符串。注意，某些子字符串可能是重复的，但你统计时也必须算上这些重复的子字符串（也就是说，你必须统计 s 的所有子字符串中的唯一字符）。

由于答案可能非常大，请将结果 mod 10 ^ 9 + 7 后再返回。


## 代码实现

1.
```python
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = collections.defaultdict(list) 
        for i, c in enumerate(s): 
            index[c].append(i) 
        
        ans = 0 
        for A in index.values(): 
            A = [-1] + A + [len(s)] 
            for i in range(1, len(A) - 1): 
                ans += (A[i] - A[i-1]) * (A[i+1] - A[i])
        return ans % (10**9 + 7)
```


## 思路总结

我们直接对于每个字符 c，计算出仅包含 c 一次的子串个数。使用和方法一相同的例子，考虑字母 "A"，并且有 S[10] = S[14] = S[20] = "A"，我们可以计算出仅包含 S[14] 的子串个数为 4 * 6 = 24，其中 4 表示子串的开始位置可以选择 11, 12, 13, 14，6 表示子串的结束位置可以选择 14, 15, 16, 17, 18, 19，根据乘法原理，子串的个数为 24。我们对于字母 "A" 出现的其它位置（例如 S[10] 和 S[20]）分别进行同样的计数，并且需要考虑边界情况，就可以得到仅包含字母 "A" 一次的子串个数。

最后对于每个字符 c，将计数结果进行累加，就得到了最终的答案。
