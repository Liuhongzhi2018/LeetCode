#  Contains Duplicate II

## 问题分析
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。


## 代码实现
``` C
bool containsNearbyDuplicate(int* nums, int numsSize, int k) {
    int n = numsSize;
    if (n<=1)return false;
    int i,j;
    for (i = 0; i<n - 1; i++){
        for (j = i + 1; (j <= i + k) && (j<n); j++){
            if (nums[i] == nums[j])
                return true;
        }
    }
    return false;
}
```

## 总结体会

本题要求判断在给定的整数数组中是否存在重复元素，较上一题Contains Duplicate区别在于增加1个限制条件即两个不同索引的步长值不大于k。

采用的算法与上一题有相似之处，不同在于for嵌套循环中，j不仅应小于n，而且与索引i应该满足不超过步长k的限制。在这2个条件的限制下，如果索引i与j对应元素相等，即满足题设条件，返回true。否则没有满足条件的元素，返回false。