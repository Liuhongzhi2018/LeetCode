#  Search in Rotated Sorted Array

## 问题分析
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

You are given a target value to search. If found in the array return its index, otherwise return -1.

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

## 代码实现
``` C++
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int head= 0, end = nums.size()-1;
        while (head<=end) {
            int mid = (end-head)/2+head;
            if (nums[mid] == target)  return mid;
            if (nums[mid] < nums[end]) {
                if (nums[mid]<target && target<=nums[end])   head = mid+1;
                else  end = mid-1;
            }
            else {
                if(nums[head]<=target && target<nums[mid])  end = mid-1;
                else  head = mid+1;
            }
        }
        return -1;
    }
};
```

## 总结体会

本题要求判断经过旋转的升序数组中是否可以找到指定的目标值并返回。

在算法设计上，采用二分查找法，首先判断中间元素是否为目标值；其次若中间值小于数列最右数字且目标值在二者之间，则在其中查找，否则在前半段查找；若中间值大于最后数字且目标值在前半段则修改范围继续查找。最后若目标值在数列内则返回，否则返回-1。
