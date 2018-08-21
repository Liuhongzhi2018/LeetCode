#  Jump Game

## 问题分析
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

## 代码实现
``` C++
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int i=0;
        int cur;
        int len=nums.size();
        for(cur=0;i<len&&i<=cur;i++){
            cur=max(i+nums[i],cur);
        }
        return i==len;
    }
};
```

## 总结体会

本题要求判断是否可以从数组的第一个位置跳到第二个位置，每次跳动的距离是当前元素值。

在算法设计上，首先初始化2个变量i和cur，分别作为数组计数器和当前数组位置；其次在for循环中，求得数组可以到达的最远距离，且i可以遍历到数组最后位置；如果i能够指向数组最后一个元素，则说明该数组满足题目要求，可以到达数组最后一个位置。
