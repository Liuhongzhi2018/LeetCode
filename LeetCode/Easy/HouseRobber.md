#  House Robber

## 问题描述

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。


## 代码实现

1.
``` C
int max(int a, int b) {
    if (a > b) return a;
    else return b;
}
int rob(int* nums, int numsSize) {
    if (numsSize <= 0)  return 0;
    if (numsSize == 1)  return *nums;
    int pre = *nums;
    int mon = max(*nums, *(nums+1));
    for (int i = 2; i<numsSize; i++) {
        int comp = max(mon,pre + nums[i]);
        pre = mon;
        mon = comp;
    }
    return mon;
}
```

2.动态规划
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        size = len(nums)
        if size == 1:
            return nums[0]
        
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = nums[1] if nums[0] < nums[1] else nums[0]
        for i in range(2, size):
            dp[i] = dp[i-2] + nums[i] if dp[i-2] + nums[i] > dp[i-1] else dp[i-1]
        return dp[size-1]

```

3.滚动数组
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        first = nums[0]
        second = nums[1] if nums[0]<nums[1] else nums[0]

        for i in range(2, size):
            first, second = second, first + nums[i] if second < first + nums[i] else second
        return second
```

## 思考总结

本题的实际背景转换为数学条件，即从一个非负整数组中求得最大不相邻元素之和。

在算法设计上，用max函数用于返回较大值，在rob函数中用for循环遍历数组元素，不相邻元素之和的较大值保存在comp变量中，每进行一次循环都将对pre和mon重新赋值，保持较大值为mon，最后将mon值返回即为偷窃的最高金额。

动态规划法，首先考虑最简单的情况。如果只有一间房屋，则偷窃该房屋，可以偷窃到最高总金额。如果只有两间房屋，则由于两间房屋相邻，不能同时偷窃，只能偷窃其中的一间房屋，因此选择其中金额较高的房屋进行偷窃，可以偷窃到最高总金额。  
如果房屋数量大于两间，应该如何计算能够偷窃到的最高总金额呢？对于第 k (k>2) 间房屋，有两个选项：

    偷窃第 k 间房屋，那么就不能偷窃第 k−1 间房屋，偷窃总金额为前 k−2间房屋的最高总金额与第 k间房屋的金额之和。

    不偷窃第 k 间房屋，偷窃总金额为前 k−1 间房屋的最高总金额。

在两个选项中选择偷窃总金额较大的选项，该选项对应的偷窃总金额即为前 k 间房屋能偷窃到的最高总金额。

用 dp[i]表示前 i 间房屋能偷窃到的最高总金额，那么就有如下的状态转移方程：dp[i]=max⁡(dp[i−2]+nums[i],dp[i−1])

滚动数组法，考虑到每间房屋的最高总金额只和该房屋的前两间房屋的最高总金额相关，因此可以使用滚动数组，在每个时刻只需要存储前两间房屋的最高总金额。