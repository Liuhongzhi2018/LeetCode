#  Single Element in a Sorted Array

## 问题分析

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。


## 代码实现

1. 暴力法
``` python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums)-2, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]
```

2. 二分搜索
```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi -lo) // 2
            halves_are_even = (hi - mid) % 2 == 0
            if nums[mid+1] == nums[mid]:
                if halves_are_even:
                    lo = mid + 2
                else:
                    hi = mid - 1
            elif nums[mid-1]==nums[mid]:
                if halves_are_even:
                    hi = mid -2
                else:
                    lo = mid + 1
            else:
                return nums[mid]
        return nums[lo]
```

3. 仅对偶数索引进行二分搜索
```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid+1]:
                lo = mid + 2
            else:
                hi = mid
        return nums[lo]
```


## 总结体会

暴力法。我们可以使用线性搜索来检查数组中的每个元素，直到找到单个元素。
算法：从第一个元素开始，我们检查每个第二个元素是否与当前元素相同。 如果不同，说明该元素是单个元素。如果我们到达最后一个元素，则它为单一元素。

二分搜索法。我们将线性搜索转换为二分搜索是有意义的，它能加快我们的效率。为了使用二分搜索，我们需要查看中间的元素来判断我们的答案在中间，左边还是右边。我们的数组个数始终是奇数，因为有一个元素出现一次，其余元素出现两次。  
我们首先将 lo 和 hi 指向数组首尾两个元素。然后进行二分搜索将数组搜索空间减半，直到找到单一元素或者仅剩一个元素为止。当搜索空间只剩一个元素，则该元素就是单个元素。  
在每个循环迭代中，我们确定 mid，变量 halvesAreEven = (hi - mid) % 2 == 0。 通过查看中间元素同一元素为哪一个（左侧子数组中的最后一个元素或右侧子数组中的第一个元素），我们可以通过变量 halvesAreEven 确定现在哪一侧元素个数为奇数，并更新 lo 和 hi。