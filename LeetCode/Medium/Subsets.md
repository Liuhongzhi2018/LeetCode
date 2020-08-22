#  Subsets

## 问题描述

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

## 代码实现

1.递归法
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]

        for num in nums:
            output += [curr + [num] for cur in output]

        return output
```

2. 回溯法
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        output = []
        n = len(nums)

        def backtrack(first=0, cur=[]):
            if len(cur) == k:
                output.append(cur[:])

            for i in range(first, n):
                cur.append(nums[i])
                backtrack(i+1, cur)
                cur.pop()

        for k in range(n+1):
            backtrack()
        return output
```


## 思路总结

递归法。开始假设输出子集为空，每一步都向子集添加新的整数，并生成新的子集。

回溯法是一种探索所有潜在可能性找到解决方案的算法。如果当前方案不是正确的解决方案，或者不是最后一个正确的解决方案，则回溯法通过修改上一步的值继续寻找解决方案。  
定义一个回溯方法 backtrack(first, curr)，第一个参数为索引 first，第二个参数为当前子集 curr。  
如果当前子集构造完成，将它添加到输出集合中。否则，从 first 到 n 遍历索引 i。将整数 nums[i] 添加到当前子集 curr。继续向子集中添加整数：backtrack(i + 1, curr)。从 curr 中删除 nums[i] 进行回溯。