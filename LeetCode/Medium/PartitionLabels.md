#  Partition Labels

## 问题描述

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。


## 代码实现

1.
``` python
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i,c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = j if j > last[c] else last[c]
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans
```


## 思路总结

思路  
策略就是不断地选择从最左边起最小的区间。可以从第一个字母开始分析，假设第一个字母是 'a'，那么第一个区间一定包含最后一次出现的 'a'。但第一个出现的 'a' 和最后一个出现的 'a' 之间可能还有其他字母，这些字母会让区间变大。举个例子，在 "abccaddbeffe" 字符串中，第一个最小的区间是 "abccaddb"。
通过以上的分析，我们可以得出一个算法：对于遇到的每一个字母，去找这个字母最后一次出现的位置，用来更新当前的最小区间。

算法  
定义数组 last[char] 来表示字符 char 最后一次出现的下标。定义 anchor 和 j 来表示当前区间的首尾。如果遇到的字符最后一次出现的位置下标大于 j， 就让 j=last[c] 来拓展当前的区间。当遍历到了当前区间的末尾时(即 i==j )，把当前区间加入答案，同时将 start 设为 i+1 去找下一个区间。
