# Two Sum
## 问题分析

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。



## 代码实现
1.用时最少，通过一次循环，找到另一个元素的下标位置
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,num in enumerate(nums):
            if hashmap.get(target - num) is not None:
               return [i,hashmap.get(target - num)]
            hashmap[num] = i
```

2.通过字典来模拟哈希查询的过程,字典记录了 num1 和 num2 的值和位置，而省去再查找 num2 索引的步骤
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,num in enumerate(nums):
            hashmap[num] = index   # 2:0
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i != j:
                 return [i,j]
```

3.遍历列表找到另一个元素值，范围是从开始到当前列表下标范围内进行查找
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = -1
        for i in range(len(nums)):
            select = nums[:i]
            if (target - nums[i]) in select:
                j = select.index(target - nums[i])
                break
        if j >= 0:
            return [j,i]
```

4.找出满足目标和的另一个元素，当存在另一个元素时再进行判断。
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = -1
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                if (nums.count(target - nums[i]) == 1) & (target - nums[i] == nums[i]):
                     continue
                else:
                    j = nums.index(target - nums[i], i+1)
                    break
        if j > 0:
            return [i,j]
        else:
            return []

```

5.两层循环，测试时超出时间限制
``` python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    result.append(i)
                    result.append(j)
        return result
```

## 总结体会
本题考察两数之和，确定下标位置

知识补充：
python3参数中的冒号与箭头。其作用是提高代码可读性，暗示传入参数及返回数据的类型。冒号后面是建议传入的参数类型，箭头后面是建议函数返回的类型。
list.index()从列表中找出某个值第一个匹配项的索引位置。
list.count()统计某个元素在列表中出现的次数。

哈希算法是最适合的求解问题是查找与给定值相等的方法，python中用字典方式进行模拟。
