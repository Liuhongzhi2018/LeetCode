# Find Smallest Letter Greater Than Target

## 问题描述

Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'. 

给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。

在比较时，字母是依序循环出现的。举个例子：如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'。


## 代码实现

1.动态规划
``` python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lenl = len(letters)
        res = None
        com = 26
        for s in letters:
            if s == target:
                continue
            comp = ord(s) - ord(target)
            if comp < 0:
                comp = comp + 26
            if comp < com:
                com = comp
                res = s
        return res   
```

2.记录存在的字母
```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        seen = set(letters)
        for i in range(1,26):
            cand = chr((ord(target)-ord('a')+i) % 26 + ord('a'))
            if cand in seen:
                return cand
```

3.线性扫描
```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for c in letters:
            if c > target:
                return c
        return letters[0]
```

4.二分查找
```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]
```

## 思路总结

记录存在的字母：我们可以扫描 letters 记录字母是否存在。我们可以用大小为 26 的数组或者 Set 来实现。然后，从下一个字母（从比目标大一个的字母开始）开始检查一下是否存在。如果有的话则是答案。

线性扫描算法：由于 letters 已经有序，当我们从左往右扫描找到比目标字母大字母则该字母就是答案。否则(letters 不为空)答案将是 letters[0]。
