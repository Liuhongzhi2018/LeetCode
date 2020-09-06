#  Longest Mountain in Array

## 问题描述

我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：

    B.length >= 3
    存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

（注意：B 可以是 A 的任意子数组，包括整个数组 A。）

给出一个整数数组 A，返回最长 “山脉” 的长度。

如果不含有 “山脉” 则返回 0。



## 代码实现

1.双指针
```python
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        N = len(A) 
        ans = base = 0 
        while base < N: 
            end = base 
            if end + 1 < N and A[end] < A[end + 1]: 
                #if base is a left-boundary 
                #set end to the peak of this potential mountain 
                while end+1 < N and A[end] < A[end+1]: 
                    end += 1 
                
                if end + 1 < N and A[end] > A[end + 1]: 
                    #if end is really a peak.. 
                    #set 'end' to right-boundary of mountain 
                    while end+1 < N and A[end] > A[end+1]: 
                        end += 1 
                        #record candidate answer 
                        ans = max(ans, end - base + 1) 
            base = max(end, base + 1) 
        return ans
```


## 思路总结

双指针  
思路  
一般情况下，一座山脉只能在前一座山脉结束后开始。  
如果一座山脉从前一座山脉的山顶左边开始，那么此山脉长度一定小于前一座山脉。如果它从前一座山脉的山顶右边开始，那么它无法形成山脉。

算法  
假设一座山脉的起始索引为 base，山脉为 A[base], A[base+1], ..., A[end]。  
如果存在这样一座山脉，那么下一座山脉的起始索引为 base = end。如果不存在以 base 起始的山脉，要么是到了数组末尾，要么是因为 A[base] > A[base+1]，山脉的起始索引为 base + 1。