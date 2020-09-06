# K-diff Pairs in an Array

## 问题描述

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k. 

给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j), 其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k.



## 代码实现

1.快慢双指针
```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        p = set()
        # sorted(list((nums)))
        nums = sorted(nums)
        i = 0
        j = i + 1
        count = 0
        while i <= j and j < len(nums):
            if nums[j] - nums[i] == k and (nums[i], nums[j]) not in p and i != j:
                count += 1
                p.add((nums[i], nums[j]))
                j += 1
            elif nums[j] - nums[i] > k:
                i += 1
            else:
                j += 1
        return count
```

## 思考总结

快慢双指针法，首先对整数数组按照从小到大排序；然后定义快慢指针，用p集合保存整数对结果；在循环里进行判断，如果指针指向元素之差为给定k值且指针不重合，则计算器加1，最后返回计算器值。
