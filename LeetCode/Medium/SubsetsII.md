#  Subsets II

## 问题描述

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

## 代码实现

1.回溯法
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        cur = []

        def backtrack(i, cur):
            res.append(cur[:])
            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]:
                    continue
                cur.append(nums[j])
                backtrack(j+1, cur)
                cur.pop()

        backtrack(0, cur)
        return res
        
```



## 思路总结

相对其子问题而言，本题需要排序+去重：  
(1)排序sort大法谁都会；  
(2)去重可以在搜索函数中加入条件语句，continue即可