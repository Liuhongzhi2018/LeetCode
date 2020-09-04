#  Intersection of Two Arrays II

## 问题分析

Given two arrays, write a function to compute their intersection.

Note: Each element in the result should appear as many times as it shows in both arrays. The result can be in any order.

给定两个数组，写一个方法来计算它们的交集。

注意：输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。我们可以不考虑输出结果的顺序。

## 代码实现

1.
``` C++
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        int len1 = (int)nums1.size(), len2 = (int)nums2.size();
        int i = 0, j = 0;
        vector<int> res;
        while(i < len1 && j < len2){
            if(nums1[i] == nums2[j]) {
                res.push_back(nums1[i]);
                i++;
                j++;
            }
            else if(nums1[i] > nums2[j])   j++;
            else  i++;
        }
        return res;
    }
};
```

2.
```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        c1 = Counter(nums1)
        ans = []
        for n in nums2:
            if n in c1 and c1[n] > 0:
                ans.append(n)
                c1[n] -= 1
        return ans
```

## 总结体会

本题要求两个数组交集，与上一题不同的是元素在两个数组中出现的次数一致，而不是只保留一个元素。

在算法设计上，首先将给定的数组排序，其次i索引nums1数组，j索引nums2数组，直到某一数组遍历完毕。若当前元素值nums1大于nums2，则j后移；若nums1小于nums2，则i后移；否则i和j都后移。

本地关键： 本题求的是两个数组的交集，但是需要考虑重复元素。  
首先在Hash表中记录nums1中数字出现的次数，然后遍历nums2，如果数字在hash表中的次数大于0，将该数字记录到结果中。