#  Move Zeroes

## 问题分析

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note: You must do this in-place without making a copy of the array. Minimize the total number of operations.


给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

说明: 必须在原数组上操作，不能拷贝额外的数组。尽量减少操作次数。

## 代码实现

1.
``` C
void moveZeroes(int* nums, int numsSize) {
    int i, j = 0, n = numsSize;
    for (i = 0; i < n; i++) {
        if (nums[i])
            nums[j++] = nums[i];
    }
    for (j; j < n; j++)
        nums[j] = 0;
}
```

2.
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nlen = len(nums)
        if not nlen:
            return []
        newlist = []
        zcount = 0
        for i in nums:
            if i != 0:
                newlist.append(i)
            else:
                zcount += 1
        while zcount:
            newlist.append(0)
            zcount -= 1
        nums[:] = newlist

```

3.双指针
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        zindex = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[zindex] = nums[i]
                zindex += 1
            
        for i in range(zindex, len(nums)):
            nums[i] = 0
```

4.前后双指针
```
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nlen = len(nums)
        for lp in range(nlen-1):
            if nums[lp] != 0:
                continue
            else:
                rp = lp + 1
                while rp < nlen:
                    if nums[rp] != 0:
                        nums[lp], nums[rp] = nums[rp], nums[lp]
                        break
                    else:
                        rp += 1
```

## 总结体会

本题要求在给定数组保持非零元素相对顺序不变的前提下，将所有0元素移动到末尾，实际上是依次找到非零元素并将其从头开始放入数组中。

在算法设计上，首先遍历数组元素，在原数组中若非零，则挑选出来在数组中重新排列出来。其次将数组后面剩余位置补零，得到的数组即为排列要求的数组。满足在原数组操作且操作次数较少的题目说明要求，复杂度主要取决于非零元素个数，第一次OJ可以Accepted。

这个问题属于 “数组变换” 的一个广泛范畴。这一类是技术面试的重点。主要是因为数组是如此简单和易于使用的数据结构。遍历或表示不需要任何样板代码，而且大多数代码将看起来像伪代码本身。

问题的两个要求是：

    将所有 0 移动到数组末尾。
    所有非零元素必须保持其原始顺序。

这里很好地认识到这两个需求是相互排斥的，也就是说，你可以解决单独的子问题，然后将它们组合在一起以得到最终的解决方案。
