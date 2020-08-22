#  Target Sum

## 问题描述

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

## 代码实现

1.动态规划
```python
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if nums[0] == 0: 
            dic = {0: 2} 
        else:
            dic = {-nums[0]: 1, nums[0]: 1} 
            
        for i in nums[1:]: 
            r = {} 
            for j in dic: 
                p = (j+i) 
                q = (j-i) 
                if p in r: 
                    r[p] += dic[j] 
                else: 
                    r[p] = dic[j] 
                if q in r: 
                    r[q] += dic[j] 
                else: 
                    r[q] = dic[j] 
            dic = r 
        res = 0 
        if S in dic: 
            res = dic[S] 
        return (res)
```


## 思路总结

