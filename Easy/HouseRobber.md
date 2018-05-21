#  House Robber

## 问题分析
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。


## 代码实现
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

## 总结体会

本题的实际背景转换为数学条件，即从一个非负整数组中求得最大不相邻元素之和。

在算法设计上，用max函数用于返回较大值，在rob函数中用for循环遍历数组元素，不相邻元素之和的较大值保存在comp变量中，每进行一次循环都将对pre和mon重新赋值，保持较大值为mon，最后将mon值返回即为偷窃的最高金额。