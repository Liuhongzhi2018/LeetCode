#  Jump Game II

## 问题分析

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Note:

You can assume that you can always reach the last index.

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

说明:

假设你总是可以到达数组的最后一个位置。

## 代码实现

1.
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        new_max,maxi,stp = 0,0,0
        for i in range(len(nums)-1):
            num = nums[i]
            new_max = max(new_max,i+num)
            if i == maxi:
                stp += 1
                maxi = new_max
                if maxi >= len(nums)-1:
                    break
        return stp
```


## 思路总结

第一步从下标为0的元素开始跳跃，在范围内找到第二步跳可以到达的最远位置，存储在new_max当中；  
以此类推，跳到最后位置。
