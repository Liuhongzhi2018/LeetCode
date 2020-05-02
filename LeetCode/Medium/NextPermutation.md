#   Next Permutation

## 问题分析
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

## 代码实现
``` C++
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i,j,len,tmp;
        len=nums.size();
        i=len-1;
        while(i>0 &&nums[i]<=nums[i-1])  i--;
        if(i>0){
            j=len-1;
            while(j>=i && nums[j]<=nums[i-1])  j--;
            tmp=nums[i-1];
            nums[i-1]=nums[j];
            nums[j]=tmp;
        }
        j=len-1;
        while(i<j){
            tmp=nums[i];
            nums[i]=nums[j];
            nums[j]=tmp;
            i++;
            j--;
        }
    }
};
```

## 总结体会
本题要求根据所给数组的元素，找到比其大的最小数组排列，或者是字典排序的最小排列。

在算法设计上，首先找到数组元素中从左到右第一个升序的元素，该元素比右边元素小，若没有则说明此数组是字典排序最大值，应返回数组排列最小值；其次若存在升序排列，则找到该元素右边比其大的最小数互换，即为所求；若不存在升序排列，则将数组反向输出即为最小排列。


