# Merge Sorted Array

## 问题分析
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note: The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。


## 代码实现
``` C
void merge(int* nums1, int m, int* nums2, int n) {
	int i = m - 1;
	int j = n - 1;
	int k = m + n - 1;
	for (k; k >= 0; k--) {
		if (j < 0)  nums1[k] = nums1[i--];
		else if (i < 0)  nums1[k] = nums2[j--];
		else if (nums1[i] > nums2[j]) nums1[k] = nums1[i--];
		     else  nums1[k] = nums2[j--];
		
	}
}
```

## 总结体会
本题主要考察两个有序数组元素大小比较以及重组有序数组。

利用题目条件中一个数组足够大，即用来保存有序数组元素，然后数组间元素逆序遍历大小比较，保存较大的元素。

难点在于if else 条件判断语句的先后顺序，如果i与j小于0，即数组指针已经不指向数组元素中的条件放后判断会产生指向不明，因此需要放在大小比较前。其次需要掌握if else嵌套逻辑含义正确使用。



