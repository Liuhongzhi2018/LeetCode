#  Circular Array Loop

## 问题描述

You are given a circular array nums of positive and negative integers. If a number k at an index is positive, then move forward k steps. Conversely, if it's negative (-k), move backward k steps. Since the array is circular, you may assume that the last element's next element is the first element, and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in nums. A cycle must start and end at the same index and the cycle's length > 1. Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not consist of both forward and backward movements.

给定一个含有正整数和负整数的环形数组 nums。 如果某个索引中的数 k 为正数，则向前移动 k 个索引。相反，如果是负数 (-k)，则向后移动 k 个索引。因为数组是环形的，所以可以假设最后一个元素的下一个元素是第一个元素，而第一个元素的前一个元素是最后一个元素。

确定 nums 中是否存在循环（或周期）。循环必须在相同的索引处开始和结束并且循环长度 > 1。此外，一个循环中的所有运动都必须沿着同一方向进行。换句话说，一个循环中不能同时包括向前的运动和向后的运动

## 代码实现

1.快慢指针
```python
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        nxt = lambda x: (x + nums[x]) % n
        
        for i in range(n):
            if nums[i] == 0: continue
            slow = i
            fast = nxt(i)

            while nums[slow] * nums[fast] > 0 and nums[fast] * nums[nxt(fast)] > 0:
                if slow == fast:
                    if slow == nxt(slow):
                        break
                    else:
                        return True
                slow = nxt(slow)
                fast = nxt(nxt(fast))

            val = nums[i]
            while val * nums[i] > 0:
                tmp = nxt(i)
                nums[i] = 0
                i = tmp
        return False
```

2. 快慢指针
```python
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        # nxt = lambda x: (x + nums[x]) % n
        def nxt(x):
            return (x + nums[x]) % n
        
        for i in range(n):
            if nums[i] == 0: continue
            slow = i
            fast = nxt(i)

            while nums[slow] * nums[fast] > 0 and nums[fast] * nums[nxt(fast)] > 0:
                if slow == fast:
                    if slow == nxt(slow):
                        break
                    else:
                        return True
                slow = nxt(slow)
                fast = nxt(nxt(fast))

            val = nums[i]
            while val * nums[i] > 0:
                tmp = nxt(i)
                nums[i] = 0
                i = tmp
        return False
```


## 思路总结

lambda简化了函数定义的书写形式，使代码更为简洁。  
lambda作为一个表达式，定义了一个匿名函数，上例的代码x为入口参数，返回(x + nums[x]) % n 值。  
快慢指针方法，用nxt函数计算得到 x 的下一个位置，通过快慢指针确定是否存在环，将访问过的元素置为0。