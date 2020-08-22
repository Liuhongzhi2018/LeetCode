#  Wiggle Subsequence

## 问题描述

A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。

例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。

给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。


## 代码实现

1.动态规划
```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n=len(nums) 
        if n<2: 
            return n 
        up=[nums[0]] 
        down=[nums[0]] 
        for i in range(1,n): 
            if nums[i]>nums[i-1]: 
                up=down+[nums[i]] 
            elif nums[i]<nums[i-1]: 
                down=up+[nums[i]] 
            else: continue 
        return max(len(up),len(down))
```


## 思路总结

up结尾的摆动序列是由最长的以down结尾的序列转化过来  
down结尾的摆动序列是由最长的以up结尾的序列转化过来  
动态规划方法up和down分别记录了末尾up结尾的最长摆动序列和down结尾的最长摆动序列