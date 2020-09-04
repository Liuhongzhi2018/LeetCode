#  Intersection of Two Arrays

## 问题分析

Given two arrays, write a function to compute their intersection.

Note: Each element in the result must be unique. The result can be in any order.

给定两个数组，写一个函数来计算它们的交集。

提示: 每个在结果中的元素必定是唯一的。 我们可以不考虑输出结果的顺序。

## 代码实现

1.
``` C
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    int len1 = nums1Size;
    int len2 = nums2Size;
    int *inter = (int *)malloc(sizeof(int) * (len1 > len2 ? len1 : len2));
    if (len1 == 0 || len2 == 0) return inter;
    memset(inter, 0, sizeof(inter));
    int num1[100010];
    int num2[100010];
    memset(num1, 0, sizeof(num1));
    memset(num2, 0, sizeof(num2));
    int i, count = 0;
    int max1 = nums1[0], max2 = nums2[0];
    for (i = 0; i < len1; i++) {
        if (nums1[i] > max1) max1 = nums1[i];
        num1[nums1[i]] = 1;
    }
    for (i = 0; i < len2; i++) {
        if (nums2[i] > max2) max2 = nums2[i];
        num2[nums2[i]] = 1;
    }
    int MAX = max1 > max2 ? max1 : max2;
    for (i = 0; i <= MAX; i++) {
        if (num1[i] && num2[i]) {
            inter[count++] = i;
        }
    }
    *returnSize = count;
    return inter;
}
```

2.内置函数
```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)
```

3.两个set
```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        def set_intersection(s1, s2):
            return [x for x in set1 if x in set2]
        
        if len(set1) < len(set2):
            return set_intersection(set1,set2)
        else:
            return set_intersection(set2,set1)
        
```

## 总结体会

本题要求两个数组交集，且不出现重复的元素，主要进行数组元素遍历和找出共同数组元素。

在算法设计上，首先初始化一个数组inter用于保存交集的数组元素，存储空间大小与最大数组相同；其次num1和num2数组中将nums1和nums2中最大元素下对应元素位置赋值1；最后遍历数组num1和num2，两个同做与运算，交集元素保存在inter数组中返回。

Python 提供了可用于求交集的 & 运算符，如果使用内置函数：那么平均情况下，时间复杂度为 O(n+m)；而最坏的情况下，时间复杂度是 O(n × m) 。

为了在线性时间内解决这个问题，我们使用集合 set 这一数据结构，该结构可以提供平均时间复杂度为 O(1) 的 in/contains 操作（用于测试某一元素是否为该集合的成员）。  
本解法先将两个数组都转换为集合，然后迭代较小的集合，检查其中的每个元素是否同样存在于较大的集合中。平均情况下，这种方法的时间复杂度为 O(n+m) 。