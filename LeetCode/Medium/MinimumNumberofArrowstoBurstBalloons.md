#  Minimum Number of Arrows to Burst Balloons

## 问题分析

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以y坐标并不重要，因此只要知道开始和结束的x坐标就足够了。开始坐标总是小于结束坐标。平面内最多存在104个气球。

一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。



## 代码实现

1.贪心算法
```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return len(points)
        newball = sorted(points, key=lambda x:x[1])
        arrow = 1
        p = newball[0]
        for ball in newball[1:]:
            if ball[0] > p[1]:
                p = ball
                arrow += 1
        return arrow
```



## 总结体会

与435题无重叠区间类似，区别在于这里需要计算不重叠区间的个数，且对于区间交集只有端点情形计作重叠
