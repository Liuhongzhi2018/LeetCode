#  Product of Array Except Self

## 问题描述

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。


## 代码实现

1.
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums) 
        answer = [0]*length 
        
        # answer[i] 表示索引 i 左侧所有元素的乘积 
        # 因为索引为 '0' 的元素左侧没有元素， 所以 answer[0] = 1 
        answer[0] = 1 
        for i in range(1, length): 
            answer[i] = nums[i - 1] * answer[i - 1] 
        
        # R 为右侧所有元素的乘积 
        # 刚开始右边没有元素，所以 R = 1 
        R = 1; 
        for i in reversed(range(length)):    
            # 对于索引 i，左边的乘积为 answer[i]，右边的乘积为 R 
            answer[i] = answer[i] * R 
            # R 需要包含右边所有的乘积，所以计算下一个结果时需要将当前值乘到 R 上 
            R *= nums[i] 
        
        return answer
```

2.
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        l, r = [1] * n, [1] * n 
        
        for i in range(1, n): 
            l[i] = l[i - 1] * nums[i - 1] 
        
        for i in range(n - 2, -1, -1): 
            r[i] = r[i + 1] * nums[i + 1] 
            
        res = [] 
        for i in range(n): 
            res.append(l[i] * r[i]) 
            
        return res
```


## 思路总结

https://leetcode-cn.com/problems/product-of-array-except-self/solution/gan-jue-da-bu-fen-ti-jie-du-shi-tie-dai-ma-jia-fu-/

每个位置的结果，即为它左边的数的乘积，乘上它右边的数的乘积。
因此，我们只要申请两个数组，一个用来记录每个位置左边的乘积，和它右边的乘积，再把两个数组乘起来即可。
