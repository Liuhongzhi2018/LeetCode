# Two Sum

## 问题分析
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。


## 代码实现
1.Brute-Force
``` C
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int i,j;
    int *a = (int*)malloc(sizeof(int)*2);
    for(i = 0;i<numsSize;i++){
        for(j = i+1;(j<numsSize && j != i);j++){
            if(nums[i] + nums[j] == target){
                a[0] = i;
                a[1] = j;
            }
        }
    }
    return a;
}
```

2. Brute-Force
``` python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None
```

3. 字典模拟哈希表
``` python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for idx, num in enumerate(nums):
            cur = target - num
            if num in cache:
                return [idx, cache[num]]
            cache[cur] = idx
        return None
```

``` python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={} 
        for i,num in enumerate(nums): 
            if hashmap.get(target - num) is not None:
                return [i,hashmap.get(target - num)] 
            hashmap[num] = i
```


## 总结体会
本题要求从给定的数组中，找到相加和与目标值相等的两个数返回，根据题意只要求返回一种答案。

在算法设计上，采用for循环嵌套，用i和j两个下标，对数组元素进行遍历，i指向当前元素，j指向i后的元素，判断和与目标值是否一致，如果满足则返回i和j，即为所求的一种答案。

方法一：Brute-Force  
遍历所有的数组元素组合，如果他们的和为target，返回。  
空间复杂度：O(1)，时间复杂度：O(n^2)
 

方法二：用容器cache缓存需要找寻的值  
遍历所有的数组元素nums[i]，计算target-nums[i]，如果其在我们的容器中，则返回两者的下标。  
空间复杂度：O(n)，时间复杂度：O(n)
