#  Permutation in String

## 问题描述

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

## 代码实现

1.双指针变单指针
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lp = 0
        while lp < len(s2):
            cur = s2[lp]
            if cur not in s1:
                lp += 1
                continue
            if self.is_same(s2[lp:lp+len(s1)],s1):
                return True
            lp += 1
        return False

    def is_same(self, s1, s2):
        if len(s1) != len(s2):
            return False
        d1 = {}
        for i in s1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 0
        d2 = {}
        for i in s2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 0
        
        for i in d1.keys():
            if i not in d2 or d1[i] != d2[i]:
                return False
        
        return True
```

2.滑动窗口
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False 
        hashmap = {} 
        for i in s1: 
            if i not in hashmap: 
                hashmap[i] = 1 
            else: hashmap[i] += 1 
            
        m,n,count = len(s1),len(s2),len(s1)
        for i in range(m): 
            if s2[i] not in hashmap: 
                continue 
            elif hashmap[s2[i]]>0: 
                count-=1 
            hashmap[s2[i]]-=1 
        if count==0:
            return True 
        for i in range(n-m): 
            if s2[i] in hashmap: 
                if hashmap[s2[i]]>=0: 
                    count+=1 
                hashmap[s2[i]]+=1 
            if s2[i+m] in hashmap: 
                if hashmap[s2[i+m]]>0: 
                    count-=1 
                hashmap[s2[i+m]]-=1 
            if count==0:
                return True 
        return False
```


## 思路总结

方法一：   
1、本题窗口大小固定等于s1的长度，因此可以从双指针简化为单指针  
2、单指针遍历s2，如果当前字符不在s1中，直接跳过，进入下次循环；如果当前字符在s1中，判断从当前字符开始，一直到s1长度的子字符串是否和s1匹配(即两个字符串的字符频率是否相同)。 

方法二：滑动窗口
1 初始化滑动窗口，其长度为s1的长度；  
2 只需要判断滑动窗口中字母出现的频率是否与s1相同即可；  
3 利用哈希表储存s1中字母出现的频率，利用count总计数判断是否已经匹配；  
4 不断滑动窗口，分别对离开窗口和进入窗口的字母进行哈希表加减操作和count加减操作。