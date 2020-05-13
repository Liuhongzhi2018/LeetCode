# 4Sum

## 问题分析

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。


## 代码实现
1.
``` C
class Solution {
public:
        vector<vector<int> > fourSum(vector<int> &num, int target) {  
        vector<vector<int> > ret;  
        set<vector<int> > setter;  
        setter.clear();  
        if(num.size()<4)   return ret;  
        int i,j,k,l,sum;  
        sort(num.begin(),num.end());  
        vector<int> store(4);  
        for(i=0;i<num.size()-3;i++){  
            for(j=i+1;j<num.size()-2;j++){  
                k=j+1;  
                l=num.size()-1;  
                while(k<l){  
                    sum=num[i]+num[j]+num[k]+num[l];  
                    if(sum>target)  
                       l--;  
                    else if(sum<target)  
                            k++;  
                         else {  
                             store[0]=num[i];  
                             store[1]=num[j];  
                             store[2]=num[k];  
                             store[3]=num[l];  
                             setter.insert(store);  
                             l--;  
                             k++;  
                         }  
                }  
            }  
        }  
        set<vector<int> >::iterator it;  
        for(it=setter.begin();it!=setter.end();++it)  
            ret.push_back(*it);
        return ret;  
    }
};
```

2.重用3sum代码
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i >= 1 and nums[i]==nums[i-1]:
                continue
            new_nums = nums[i+1:]
            new_target = target-nums[i]
            tmp = self.threeSum(new_nums,new_target)
            for k in tmp:
                res.append([nums[i]]+k)
        return res

    def threeSum(self, nums, target):
        res = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i >=1 and nums[i]==nums[i-1]:
                continue
            l,r = i+1, len(nums)-1

            if nums[i] + nums[r]+nums[r-1]<target:
                continue
            if nums[i] + nums[l]+nums[l+1]>target:
                continue

            while l<r:
                tsum = nums[i]+nums[l] + nums[r]-target
                if tsum>0:
                    r -= 1
                elif tsum<0:
                    l += 1
                else:
                    if len(res)==0 or [nums[i], nums[l],nums[r]] != res[-1]:
                        res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
        return res
```

3.优化代码
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i >= 1 and nums[i]==nums[i-1]:
                continue
            if sum(nums[i:i+4])>target or nums[i]+sum(nums[-3:])<target:
                continue
            new_nums = nums[i+1:]
            new_target = target-nums[i]
            tmp = self.threeSum(new_nums,new_target)
            for k in tmp:
                res.append([nums[i]]+k)
        return res

    def threeSum(self, nums, target):
        res = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i >=1 and nums[i]==nums[i-1]:
                continue
            l,r = i+1, len(nums)-1

            if nums[i] + nums[r]+nums[r-1]<target:
                continue
            if nums[i] + nums[l]+nums[l+1]>target:
                continue

            while l<r:
                tsum = nums[i]+nums[l] + nums[r]-target
                if tsum>0:
                    r -= 1
                elif tsum<0:
                    l += 1
                else:
                    if len(res)==0 or [nums[i], nums[l],nums[r]] != res[-1]:
                        res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
        return res
```

## 总结体会
本题要求出是否存在四个元素之和与目标值相等，即遍历数组找出满足条件的4个数字的组合。

在算法设计上，首先判断是否数组元素个数是否满足不小于4；其次声明i，j，k，l作为下标，用store数组保存符合条件的元素；最后返回ret即为所求。

方法二重用3sum代码。