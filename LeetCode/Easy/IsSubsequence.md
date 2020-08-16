# Is Subsequence


## 问题分析

Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。


## 代码实现

1.双指针法
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slen, tlen = len(s), len(t)
        i = j = 0
        while i < slen and j <tlen:
            if s[i] == t[j]:
                i = i + 1
            j = j + 1
        return i == slen
```

2.动态规划
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)
        
        for i in range(m - 1, -1, -1): 
            for j in range(26): 
                f[i][j] = i if ord(t[i]) == j + ord('a') else f[i + 1][j] 
        add = 0 
        for i in range(n): 
            if f[add][ord(s[i]) - ord('a')] == m: 
                return False 
            add = f[add][ord(s[i]) - ord('a')] + 1 
        return True
```

## 总结体会

本题所求为二进制无符号位的有进位加法，难点在于动态内存分配和最高位有进位时的字符串保存。与所学数字电路中一样，二进制加法从最低位开始加起，当最高位有进位时字符串数组长度会加1，然后将字符串返回输出，即可得到加法结果。

方法一是双指针法，本题询问的是，s 是否是 t 的子序列，因此只要能找到任意一种 s 在 t 中出现的方式，即可认为 s 是 t 的子序列。而当我们从前往后匹配，可以发现每次贪心地匹配靠前的字符是最优决策。假定当前需要匹配字符 c，而字符 c 在 t 中的位出现（x1<x2x_1 < x1<x2），那么贪心取 x1是最优解，因为 x2 后面能取到的字符，x1 也都能取到，并且通过 x1 与 x2 之间的可选字符，更有希望能匹配成功
这样，我们初始化两个指针 i 和 j，分别指向 s 和 t 的初始位置。每次贪心地匹配，匹配成功则 i和 j 同时右移，匹配 s 的下一个位置，匹配失败则 j 右移，i 不变，尝试用 t 的下一个字符匹配 s。最终如果 i 移动到 s 的末尾，就说明 s 是 t 的子序列。

方法二动态规划思路及算法，考虑前面的双指针的做法，我们注意到我们有大量的时间用于在 ttt 中找到下一个匹配字符。  
这样我们可以预处理出对于 ttt 的每一个位置，从该位置开始往后每一个字符第一次出现的位置。   
我们可以使用动态规划的方法实现预处理，令 f[i][j]表示字符串 t 中从位置 i 开始往后字符 j 第一次出现的位置。在进行状态转移时，如果 t 中位置 i 的字符就是 j，那么 f[i][j]=i，否则 j 出现在位置 i+1 开始往后，即f[i][j]=f[i+1][j]，因此我们要倒过来进行动态规划，从后往前枚举 iii。  
链接：https://leetcode-cn.com/problems/is-subsequence/solution/pan-duan-zi-xu-lie-by-leetcode-solution/

