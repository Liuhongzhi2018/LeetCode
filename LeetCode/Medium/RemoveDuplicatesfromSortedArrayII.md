#  Remove Duplicates from Sorted Array II

## 问题描述

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。


## 代码实现

1.
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, count = 1, 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                count += 1

                if count > 2:
                    nums.pop(i)
                    i -= 1
            else:
                count = 1
            
            i += 1
        return len(nums)

```

2.同向双指针
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return len(nums)

        index, i = 1, 2
        while i < len(nums):
            if nums[i] != nums[index-1]:
                index += 1
                nums[index] = nums[i]
            i += 1
        return index+1
```

3.扩展,每个元素最多出现k次
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 2: return len(nums)
        k = 2
        index, i = k-1, k
        while i < len(nums):
            if nums[i] != nums[index-k+1]:
                index += 1
                nums[index] = nums[i]
            i += 1
        return index+1
```


## 思路总结

由于输入数组已经排序，所以重复项都显示在旁边。题目要求我们不使用额外的空间，在原地修改数组，而最简单的方法就是删除多余的重复项。对于数组中的每个数字，若出现 2 个以上的重复项，就将多余的重复项从数组列表中删除。

算法：
    我们需要在遍历数组元素的同时删除多余的重复项，那么我们需要在删除多余重复项的同时更新数组的索引，否则将访问到无效的元素或跳过需要访问的元素。
    我们使用两个变量，i 是遍历数组的指针，count 是记录当前数字出现的次数。count 的最小计数始终为 1。
    我们从索引 1 开始一次处理一个数组元素。
    若当前元素与前一个元素相同，即 nums[i]==nums[i-1]，则增加计数 count++。若 count > 2，则说明遇到了多余的重复元素 ，要从数组中删除它。由于我们知道这个元素的索引，可以使用 del，pop 或 remove 操作（或你选择语言支持的任何相应的操作）从数组中删除它。由于删除了一个元素，所以我们的索引应该要减一。
    若当前元素与前一个元素不相同，即 nums[i] != nums[i - 1]，说明我们遇到了一个新元素，则更新 count = 1。
    由于我们从原始数组中删除了所有多余的重复项，所以最终在原数组只保留了有效元素，返回数组长度。
    
同向双指针：  
如果题目要求每个元素最多出现k次代码怎么写。  
其实就是对于指针运动条件的考量，什么时候需要移动index指针?  
1.nums[i] != nums[index] 表示当前遍历的位置i和不重复集合的右边界不一样，那么肯定能放入不重复集合了。  
2.题目要求每个元素最多出现k次,那么如果nums[i] != nums[index-k+1] 就可以保证不会存在连续的k个元素是值是重复的。