#  Minimum Moves to Equal Array Elements II

## 问题描述

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。


## 代码实现

1.
```python
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort() 
        mid = len(nums) // 2 
        candidates = [nums[mid]] 
        if len(nums) % 2 == 0: 
            candidates.append(nums[mid - 1]) 
        ret = [0 for _ in range(len(candidates))]
        for num in nums: 
            for i, c in enumerate(candidates): ret[i] += abs(c - num) 
        return ret[0] if len(ret) == 1 else min(*ret)
```


## 思路总结

这是个典型的相遇问题，移动距离最小的方式是所有元素都移动到中位数。理由如下：

设 m 为中位数。a 和 b 是 m 两边的两个元素，且 b > a。要使 a 和 b 相等，它们总共移动的次数为 b - a，这个值等于 (b - m) + (m - a)，也就是把这两个数移动到中位数的移动次数。

设数组长度为 N，则可以找到 N/2 对 a 和 b 的组合，使它们都移动到 m 的位置。

找规律发现本质上是找到中位数。然后求所有数字到中位数的距离之和。  
只要确定的数字偏离中位数，与水平线围出的面积必然增大。