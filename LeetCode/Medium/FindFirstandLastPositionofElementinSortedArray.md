#   Find First and Last Position of Element in Sorted Array

## 问题分析

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

## 代码实现

1.
``` C++
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n=nums.size();
        if(n<1)  return {-1,-1};
        int first=findFirst(nums,target);
        int last=findLast(nums,target);
        return {first,last};
    }
    int findFirst(vector<int>& nums, int target){
        int left=0,right=nums.size()-1;
        int mid;
        while(left<=right){
            int mid=(left+right)/2;
            if(nums[mid]<target)   left=mid+1;
            else  right=mid-1;
        }
        if(left<nums.size()&&nums[left]==target)
            return left;
        return -1;
    }
    int findLast(vector<int>& nums, int target){
        int left=0,right=nums.size()-1;
        int mid;
        while(left<=right){
            mid=(left+right)/2;
            if(nums[mid]<=target)  left=mid+1;
            else  right=mid-1;
        }
        if(right>=0&&nums[right]==target)
            return right;
        return -1;
    }
};
```

2.bisect二分查找包
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        from bisect import bisect_left, bisect_right
        if len(nums)==0:
            return [-1,-1]
        res = [-1,-1]
        left = bisect_left(nums,target)
        if left<len(nums) and nums[left]==target:
            res[0]=left
            res[1]=bisect_right(nums,target)-1
        return res
```

3.
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            return [nums.index(target), len(nums)-\
            (list(nums[::-1]).index(target))-1]
        except:
            return [-1,-1]

```

## 总结体会

本题要求找出目标值在数组中的位置，通过题意可知不存在则[-1,-1]，出现1次则两个相同位置，出现2次则两个不同位置。

在算法设计上，首先应该考虑数组没有元素情况，即[]时应返回[-1,-1]，是第一次编译未通过的原因；其次采用二分查找法，分别查找第一次和第二次出现的位置，用中间值mid调整搜索范围；最后返回得到的位置。

方法二python中bisect包已经实现好二分查找的功能。需要检查bisect插入的索引位置与target是否一致，如果一致则通过bisect返回右边索引。

方法三用内置的index返回index下标，然后将数组逆序得到target下标再与数组长度相减即可。