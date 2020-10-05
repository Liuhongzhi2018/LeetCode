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

2.双指针
```
class Solution:
    def trap(self, height: List[int]) -> int:
        nheight = len(height)
        lp, rp = 0, nheight-1
        maxl = maxr = rain = 0
        while lp < rp:
            if height[lp] < height[rp]:
                if height[lp] > maxl:
                    maxl = height[lp]
                else:
                    rain += maxl - height[lp]
                lp += 1
            else:
                if height[rp] > maxr:
                    maxr = height[rp]
                else:
                    rain += maxr - height[rp]
                rp -= 1
        return rain
```


## 思路总结

左右高度分别为l和r能接的雨水为 min(l,r) * len(middle) - sum(middle)。

本题通过大结构拆成几个子结构。

首先找到最高点一刀两段，得到左右两个部分；  
再找到max的位置，然后像子问题一样，计算右边的盛水量，将左边的继续迭代；  
右边部分将元素进行翻转，然后和计算左边方法一样。

双指针方法：  
直观想法  
和方法 2 相比，我们不从左和从右分开计算，我们想办法一次完成遍历。  
从动态编程方法的示意图中我们注意到，只要 right_max[i]>left_max[i]（元素 0 到元素 6），积水高度将由 left_max 决定，类似地 left_max[i]>right_max[i]（元素 8 到元素 11）。
所以我们可以认为如果一端有更高的条形块（例如右端），积水的高度依赖于当前方向的高度（从左到右）。当我们发现另一侧（右侧）的条形块高度不是最高的，我们则开始从相反的方向遍历（从右到左）。
我们必须在遍历时维护 left_max 和 right_max ，但是我们现在可以使用两个指针交替进行，实现 1 次遍历即可完成。

算法流程  

    初始化 left\text{left}left 指针为 0 并且 right\text{right}right 指针为 size-1
    While left<right\text{left}< \text{right}left<right, do:
        If height[left]\text{height[left]}height[left] < height[right]\text{height[right]}height[right]
            If height[left]≥left_max\text{height[left]} \geq \text{left\_max}height[left]≥left_max, 更新 left_max\text{left\_max}left_max
            Else 累加 left_max−height[left]\text{left\_max}-\text{height[left]}left_max−height[left] 到 ans\text{ans}ans
            left\text{left}left = left\text{left}left + 1.
        Else
            If height[right]≥right_max\text{height[right]} \geq \text{right\_max}height[right]≥right_max, 更新 right_max\text{right\_max}right_max
            Else 累加 right_max−height[right]\text{right\_max}-\text{height[right]}right_max−height[right] 到 ans\text{ans}ans
            right\text{right}right = right\text{right}right - 1.