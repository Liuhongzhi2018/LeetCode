#  Intersection of Two Arrays II

## 问题分析
Given two arrays, write a function to compute their intersection.

Note: Each element in the result should appear as many times as it shows in both arrays. The result can be in any order.

给定两个数组，写一个方法来计算它们的交集。

注意：输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。我们可以不考虑输出结果的顺序。

## 代码实现
``` Java
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        int len1 =  nums1.length;    
        int len2 =  nums2.length;    
        int[] result = new int[Math.min(len1, len2)];  
        int len = 0, i = 0, j = 0;  
        Arrays.sort(nums1);  
        Arrays.sort(nums2);  
        while (i < len1 && j < len2) {  
            if (nums1[i] == nums2[j]) {  
                result[len] =nums1[i];  
                len++;  
                i++;  
                j++;  
            }  
            else if (nums1[i] < nums2[j])   i++;  
            else   j++;  
        }  
        result = Arrays.copyOf(result, len);  
        return result;    
    }  
}
```

## 总结体会

本题要求两个数组交集，与上一题不同的是元素在两个数组中出现的次数一致，而不是只保留一个元素。

在算法设计上，首先将给定的数组排序，其次i索引nums1数组，j索引nums2数组，直到某一数组遍历完毕。若当前元素值nums1大于nums2，则j后移；若nums1小于nums2，则i后移；否则i和j都后移。

