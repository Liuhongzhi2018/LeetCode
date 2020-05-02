#  Majority Element

## 问题分析
Given an array of size n, find the majority element. The majority element is the element that appears more than [ n/2 ] times.

You may assume that the array is non-empty and the majority element always exist in the array.

给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 [ n/2 ]的元素。

可以假设数组是非空的，并且给定的数组总是存在众数。

## 代码实现
``` C
int majorityElement(int* nums, int numsSize) {
    int n = numsSize;
    if (n <= 0) return NULL;
    int i;
    int count = 0, point;
    for (i = 0; i < n; i++) {
        if (count == 0) point = nums[i];
        if (point == nums[i]) count++;
           else  count--;
    }
    return point;
}
```

## 总结体会

本题要求在一个有n个元素的数组中，找出众数。通过概念理解，应记下各元素出现的次数，出现最多的则为众数，但是采用顺序计数的算法则超时，因此需要采用其他的算法。

通过学习并采用Moore’s voting算法，从一个数组中找出半数以上的元素。在遍历数组nums[]时，如果count为0，表示当前并没有候选元素，也就是说之前的遍历过程中并没有找到超过半数的元素。如果遍历结束之后，count不为0，那么元素nums[i]即为寻找的元素。上述算法的时间复杂度为O(n)，而由于并不需要真的删除数组元素，也并不需要额外的空间来保存原始数组，空间复杂度为O(1)。

最后剩下的元素也可能并没有出现半数以上，即众数不一定要求出现次数大于[ n/2 ]，排除这种情况的方法是只要保存原始数组，最后遍历元素验证即可。













