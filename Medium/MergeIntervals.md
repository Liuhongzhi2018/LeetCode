#  Merge Intervals

## 问题分析
Given a collection of intervals, merge all overlapping intervals.

给出一个区间的集合，请合并所有重叠的区间。

## 代码实现
``` C++
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        int len = intervals.size();
        int i,cur;
        vector<Interval>meg(intervals);
        if(len>1){
            std::sort(meg.begin(),meg.end(),[](Interval i,Interval j){return i.start<j.start;});
            for(cur=0,i=1;i<len;i++)
                if(meg[cur].end<meg[i].start) meg[++cur]=meg[i];
                else meg[cur].end=max(meg[cur].end,meg[i].end);
            meg.resize(cur+1);
        }
    return meg;
    }
};
```

## 总结体会

本题要求在给定区间集合中，找到可以合并的区间进行合并。

在算法设计上，首先给区间集排序，由于对结构体排序，故先定义比较器；然后用sort从小到大来排序和合并，第一个区间存入结果中，然后从第二个开始遍历区间集，如果结果中最后一个区间和遍历的当前区间无重叠，直接将当前区间存入结果中，如果有重叠，将结果中最后一个区间的end值更新为结果中最后一个区间的end和当前end值之中的较大值，然后继续遍历区间集，以此类推可以得到最终结果；最后得到的meg即为所求的区间集合。
