#   Trapping Rain Water

## 问题分析

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 


## 代码实现

1.
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0 or max(height)==0:
            return 0
        self.res = 0
        max_ = max(height)
        index = height.index(max_)
        self.area(height[:index])
        self.area(height[index+1:][::-1])
        return self.res

    def area(self,h):
        if len(h) == 0 or max(h) == 0:
            return 
        maxh = max(h)
        index = h.index(maxh)
        self.res += ((len(h)-index-1)*maxh) \
        -sum(h[index+1:])
        self.area(h[:index])
```


## 思路总结

左右高度分别为l和r能接的雨水为 min(l,r) * len(middle) - sum(middle)。

本题通过大结构拆成几个子结构。

首先找到最高点一刀两段，得到左右两个部分；  
再找到max的位置，然后像子问题一样，计算右边的盛水量，将左边的继续迭代；  
右边部分将元素进行翻转，然后和计算左边方法一样。