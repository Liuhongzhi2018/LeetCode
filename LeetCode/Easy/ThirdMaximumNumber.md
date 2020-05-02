#  Third Maximum Number

## 问题分析
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

## 代码实现
``` C
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        long n= sizeof(nums) / sizeof(nums[0]);
        long max = LONG_MIN, mid = LONG_MIN, min = LONG_MIN;
        int i;
        for (int num : nums) {
            if (num > max) {
                min = mid;
                mid = max;
                max = num;
            } 
            else if (num > mid && num < max) {
                min = mid;
                mid = num;
            } 
            else if (num > min && num < mid) {
                min = num;
            }
        }
        return (min == LONG_MIN || min == mid) ? max : min;
    }
};
```

## 总结体会

本题要求数组中第三大的数字，若不存在则求最大数字。

在算法设计上，声明3个变量max、mid和min，分别保存最大、第二大和第三大数字。通过遍历数组元素，根据遍历的元素对3个变量赋值进行修改，直至找出对应大小的元素；若数组元素中不存在第三大的数字，将所求出的最大值返回。

