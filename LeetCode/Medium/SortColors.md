#  Sort Colors

## 问题分析

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

## 代码实现

1.
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

2. 双指针法
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        sign = 0
        for i in range(length-1):
            if sign not in nums[i:] and sign < 2:
                sign += 1
            cur = nums[i]
            if cur == sign:
                continue
            for j in range(i+1,length):
                if nums[j] == sign:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
        return nums
```

3. 一次遍历
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = curr = 0
        p1 = len(nums) - 1
        while curr <= p1:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p1] = nums[p1], nums[curr]
                p1 -= 1
            else:
                curr += 1
```

## 总结体会

本题要求从乱序的数组中，对所含的0，1，2元素进行重新排序，将它们按照顺序和相邻进行排序。

在算法设计上，首先构建辅助数组count[]，该数组用来统计0,1,2的个数；其次遍历数组，向数组中分别放入相应数量的元素；最后nums即为所求排序后的数组。

方法二是使用双指针，sign为需要排序的元素即标志位，当前位置指针保存元素为cur，如果当前元素即需要找的元素则跳过，否则后面列表中有需要交换的元素，则进行元素交换。

方法三一次遍历，用三个指针（p0, p1 和curr）来分别追踪0的最右边界，2的最左边界和当前考虑的元素。本解法的思路是沿着数组移动 curr 指针，若nums[curr] = 0，则将其与 nums[p0]互换；若 nums[curr] = 2 ，则与 nums[p1]互换。

算法  
初始化0的最右边界：p0 = 0。在整个算法执行过程中 nums[idx < p0] = 0.  
初始化2的最左边界 ：p2 = n - 1。在整个算法执行过程中 nums[idx > p2] = 2.  
初始化当前考虑的元素序号 ：curr = 0.  
While curr <= p2 :  
    若 nums[curr] = 0 ：交换第 curr个 和 第p0个 元素，并将指针都向右移。  
    若 nums[curr] = 2 ：交换第 curr个和第 p2个元素，并将 p2指针左移 。  
    若 nums[curr] = 1 ：将指针curr右移。  
