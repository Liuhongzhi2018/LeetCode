# Peak Index in a Mountain Array

## 问题描述

Let's call an array arr a mountain if the following properties hold:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... arr[i-1] < arr[i]
        arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

我们把符合下列属性的数组 A 称作山脉：

    A.length >= 3
    存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]

给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。


## 代码实现

1.二分查找
```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1 
        while l < r: 
            mid = (l + r) // 2 
            if arr[mid] < arr[mid + 1]: 
                l = mid + 1 
            else: 
                r = mid 
        return l
```

## 思考总结

将山脉数组中所有满足 A[i] < A[i+1] 的 i 点标记为 True，不满足的点标记为 False。则一个山脉数组可以标记为：[True, True, True, ..., True, False, False, ..., False]。例如山脉数组 [1, 2, 3, 4, 1] 可以标记为 True, True, True, False。

在山脉数组上使用二分查找，找出满足 A[i] < A[i+1] 的最大 i。
