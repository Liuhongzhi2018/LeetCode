#   Partition Equal Subset Sum

## 问题描述

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

    Each of the array element will not exceed 100.
    The array size will not exceed 200.

给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

    每个数组中的元素不会超过 100
    数组的大小不会超过 200



## 代码实现

1.动态规划
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        all_sum, N = sum(nums), len(nums) 
        if all_sum % 2 == 1: 
            return False 
        half_sum = all_sum // 2 
        # 必须得将nums数组排序，避免遍历flag数组的时候下标溢出 
        nums.sort() 
        # flag[i][j]: 表示nums数组前i个元素是否可以表示和为j的状态True or False
        flag = [[False]*(half_sum+1) for _ in range(N)] 
        # 只要nums中的元素可以组合成和为half_sum即可。同时也规定了元素不可以扩充使用， 
        # 这一点和0-1背包问题不同，所以第一层遍历就是遍历nums数组，避免重复 
        for i in range(N): 
            for j in range(nums[i], half_sum+1): 
                # 此状态说明当前元素恰好为j，直接返回True 
                if j == nums[i]: 
                    flag[i][j] = True 
                else: flag[i][j] = flag[i-1][j] or flag[i-1][j-nums[i]]
        return flag[-1][-1]
```


## 思路总结

