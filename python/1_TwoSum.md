# Two Sum
## 问题分析

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。



## 代码实现
``` python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
```

## 总结体会
本题考察两数之和
所求为二进制无符号位的有进位加法，难点在于动态内存分配和最高位有进位时的字符串保存。与所学数字电路中一样，二进制加法从最低位开始加起，当最高位有进位时字符串数组长度会加1，然后将字符串返回输出，即可得到加法结果。
