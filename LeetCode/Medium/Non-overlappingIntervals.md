#  Non-overlapping Intervals

## 问题分析

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

## 代码实现

1. 区间排序
``` python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if intervals == []:
            return 0
        newlist = sorted(intervals, key=lambda x: x[1])
        count = 0
        cur = newlist[0]
        for sub in newlist[1:]:
            if sub[0] < cur[1]:
                count += 1
            else:
                cur = sub
        return count 
```



## 总结体会

选择区间组成无重叠区间，为使区间数量尽可能多，被选区间的右端点应尽可能小，留给后面的区间的空间就大，那么后面能够选择的区间个数也就大。因此可以先对区间列表根据右端点排序，遍历新的列表，根据是否重叠决定是否移除区间。

首先将所给列表按照区间右端点排序，区间元素与之前选中区间进行比较，如果某一区间左端点小于当前选中区间的右端点，则计数加1。