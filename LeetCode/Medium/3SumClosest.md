#  3Sum Closest

## 问题分析
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

## 代码实现
1.
``` C
void quickSort(int* nums,int first,int end);
int threeSumClosest(int* nums, int numsSize, int target);

void quickSort(int* nums,int first,int end){
    int l=first,r=end;
    if(first>=end)return;
    int temp=nums[l];
    while(l<r){
        while(l<r && nums[r]>=temp)   r--;
        if(l<r)   nums[l]=nums[r];
        while(l<r && nums[l]<=temp)    l++;
        if(l<r)    nums[r]=nums[l];
    }
    nums[l]=temp;
    quickSort(nums,first,l-1);
    quickSort(nums,l+1,end);
}
int threeSumClosest(int* nums, int numsSize, int target) {
    int begin,end,i,sum,Min=INT_MAX;
    quickSort(nums,0,numsSize-1);
    for(i=0;i<numsSize-2;i++){
        if(i>0 && nums[i]==nums[i-1])continue;
        begin=i+1;end=numsSize-1;
        while(begin<end){
            sum=nums[i]+nums[begin]+nums[end];
            if(abs(sum-target)<abs(Min))Min=sum-target;
            if(sum==target)return target;
            else if(sum>target)end--;
            else begin++;
        }
    }
    return Min+target;
}
```

2.
```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)-2):
            if i>=1 and nums[i]==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                cur = nums[i]+nums[l]+nums[r]
                if abs(cur-target)<abs(res-target):
                    res = cur
                if cur>target:
                    r -= 1
                elif cur < target:
                    l += 1
                else:
                    return target
        return res
```

3.加速
```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)-2):
            if i>=1 and nums[i]==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            if nums[i]+nums[r-1]+nums[r] <= target:
                l = r -1
            elif nums[i]+nums[l]+nums[l+1]>=target:
                r = l+1
            while l<r:
                cur = nums[i]+nums[l]+nums[r]
                if abs(cur-target)<abs(res-target):
                    res = cur
                if cur>target:
                    r -= 1
                elif cur < target:
                    l += 1
                else:
                    return target
        return res
```

## 总结体会

本题要求根据指定的数组和目标值，求出与target差最小的整数值。

在算法设计上，先升序排序，然后用第一重for循环确定第一个数字。在第二重循环里，第二、第三个数字分别从两端往中间扫。如果三个数的total等于target，返回target。如果三个数的total大于0，所以第三个数往左移。如果三个数的total小于0，说明需要减小，所以第二个数往右移，这时更新closeTarget返回。

加速方法：给定i值，如果与最右两值和都比target小，则不需要看其他组合；如果与最左两值和都比target大，则不需要看其他组合。如果在代码里加入判断。
