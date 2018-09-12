#  Sort Colors

## 问题分析
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

## 代码实现
``` C++
class Solution {
public:
    void sortColors(vector<int>& nums) {
      int i,j;
      vector<int>count(3, 0);
      for (i = 0; i < nums.size(); i++){
        count[nums[i]]++;
      }
      nums.clear();
      for (i = 0; i < count.size(); i++){
        j = 0;
        while (j < count[i]){
          nums.push_back(i);
          j++;
        }
      }
    }
};
```

## 总结体会

本题要求从乱序的数组中，对所含的0，1，2元素进行重新排序，将它们按照顺序和相邻进行排序。

在算法设计上，首先构建辅助数组count[]，该数组用来统计0,1,2的个数；其次遍历数组，向数组中分别放入相应数量的元素；最后nums即为所求排序后的数组。
