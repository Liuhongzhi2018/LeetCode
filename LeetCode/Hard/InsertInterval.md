#  Insert Interval

## 问题分析

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。


## 代码实现

1.
```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        res = []
        tmp = intervals + [newInterval]
        tmp = list(sorted(tmp))

        low = tmp[0][0]
        high = tmp[0][1]

        for i in range(1,len(tmp)):
            if high >= tmp[i][0]:
                if high < tmp[i][1]:
                    high = tmp[i][1]

            else:
                res.append([low,high])
                low = tmp[i][0]
                high = tmp[i][1]

        res.append([low,high])
        return res
```


## 思路总结

先将newInterval插入intervals中并进行排序，之后将所有区间进行合并。  
若当前区间和目前保存区间有交集，则进行判断后修改相应的区间参数；若当前区间和目前保存区间没有交集，则将目前保存区间放入到结果集合中，并将当前区间记录成目前保存区间