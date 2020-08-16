# Non-decreasing Array

## 问题分析

Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。



## 代码实现

1.
```python
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0:
            return False
        if n < 2:
            return True
        count = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
                if i + 1 < len(nums) and i - 2 >= 0:
                    if nums[i+1] < nums[i-1] and nums[i-2] > nums[i]:
                        return False
            if count > 1:
                return False
        return True
```

## 总结体会

解题思路：遍历数组，初始count = 0，如果当前元素值比它下一个元素值大，则count += 1，当count > 1时，直接返回false。
另外，在遍历数组的过程中，如果遇到 “特殊情况”，可以直接返回false；当循环正常结束则返回true。

特殊情况解释：  
首先看一个简单的例子：[2, 4, 0, 1]  
当下标 i == 2 时，nums[i] < nums[i-1]，也就是 0 < 4，这时我们要保证数组非递减有两种选择：  
选择 1：把 0 放大，并且保证 0 后面的数不能比 4 小，0 前面的数均是非递减的；  
选择 2：把 4 缩小，并且保证 4 前面的数不能比 0 大，4 后面的数均是非递减的。  
换言之，当 0 < 4时，如果以上两个选择中的保证同时不满足，说明该数组肯定无法通过只修改一个元素而变为非递减数组，该情况即为上述提到的 “特殊情况”。对于本例，有：当 0 < 4时，0 后面的数为 1，1 小于 4，不满足选择 1 的保证；且 4 前面的数为 2，4 后面的数为 0，0 小于 2，不满足选择 2 的保证。
