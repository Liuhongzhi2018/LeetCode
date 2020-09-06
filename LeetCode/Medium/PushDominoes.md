#  Push Dominoes

## 问题描述

There are N dominoes in a line, and we place each domino vertically upright.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

一行中有 N 张多米诺骨牌，我们将每张多米诺骨牌垂直竖立。

就这个问题而言，我们会认为正在下降的多米诺骨牌不会对其它正在下降或已经下降的多米诺骨牌施加额外的力。

给定表示初始状态的字符串 "S" 。如果第 i 张多米诺骨牌被推向左边，则 S[i] = 'L'；如果第 i 张多米诺骨牌被推向右边，则 S[i] = 'R'；如果第 i 张多米诺骨牌没有被推动，则 S[i] = '.'。

返回表示最终状态的字符串。



## 代码实现

1.相邻标记
```python
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.'] 
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')] 
        ans = list(dominoes) 
        for (i, x), (j, y) in zip(symbols, symbols[1:]): 
            if x == y: 
                for k in range(i+1, j): 
                    ans[k] = x 
            elif x > y: #RL 
                for k in range(i+1, j): 
                    ans[k] = '.LR'[self.cmp(k-i, j-k)] 
        return "".join(ans)

    def cmp(self, a, b):
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1
```


## 思路总结

想法  
对于每组垂直多米诺骨牌（'.'），我们有两个非垂直多米诺骨牌将他们分割开。因为在这个组外的多米诺骨牌不会有影响，我们可以分别分析每组的情况：一共有 9 种可能（由于边界多米诺可能是空）。实际上，如果我们用 L 和 R 的多米诺骨牌作为边界，最多只有 4 种情况。我们会根据情况的不同使用新字母来表示。

算法   
继续我们的算法，我们分析以下形式：  
    如果我们有 "A....B"，当 A = B，那么就变成 "AAAAAA"。  
    如果我们有 "R....L"，那么结果会变成 "RRRLLL" 或者 "RRR.LLL" 如果点的个数是奇数。如果初始标记的坐标是 i 和 j，我们可以检查距离 k-i 和 j-k 来决定位置 k 的形态是 'L'，'R' 还是 '.'。  
    如果我们有 "L....R"，就什么都不做，跳过。