#  Combination Sum III

## 问题描述

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:  
All numbers will be positive integers.
The solution set must not contain duplicate combinations.

找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：  
所有数字都是正整数。
解集不能包含重复的组合。 



## 代码实现

1.
``` python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def DFS(num, sumn, tmp):
            if len(tmp) > k or sumn > n:
                return
            if len(tmp) == k and sumn == n:
                res.append(tmp[:])
                return
            for i in range(num+1, 10):
                if sumn + i > n:
                    break
                DFS(i, sumn+i, tmp+[i])

        DFS(0 ,0 ,[])
        return res
```


## 思路总结

回溯加剪枝，同时注意i的范围是0到9的取值范围。