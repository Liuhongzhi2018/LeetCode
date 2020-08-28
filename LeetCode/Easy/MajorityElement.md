#  Majority Element

## 问题分析

Given an array of size n, find the majority element. The majority element is the element that appears more than [ n/2 ] times.

You may assume that the array is non-empty and the majority element always exist in the array.

给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 [ n/2 ]的元素。

可以假设数组是非空的，并且给定的数组总是存在众数。

## 代码实现

1.
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

2.Boyer-Moore 投票算法
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        candidate = None 
        for num in nums: 
            if count == 0: 
                candidate = num 
            count += (1 if num == candidate else -1) 
        return candidate
```

## 总结体会

本题要求在一个有n个元素的数组中，找出众数。通过概念理解，应记下各元素出现的次数，出现最多的则为众数，但是采用顺序计数的算法则超时，因此需要采用其他的算法。

通过学习并采用Moore’s voting算法，从一个数组中找出半数以上的元素。在遍历数组nums[]时，如果count为0，表示当前并没有候选元素，也就是说之前的遍历过程中并没有找到超过半数的元素。如果遍历结束之后，count不为0，那么元素nums[i]即为寻找的元素。上述算法的时间复杂度为O(n)，而由于并不需要真的删除数组元素，也并不需要额外的空间来保存原始数组，空间复杂度为O(1)。

最后剩下的元素也可能并没有出现半数以上，即众数不一定要求出现次数大于[ n/2 ]，排除这种情况的方法是只要保存原始数组，最后遍历元素验证即可。

Boyer-Moore 投票算法思路  
如果我们把众数记为 +1+1+1，把其他数记为 −1-1−1，将它们全部加起来，显然和大于 0，从结果本身我们可以看出众数比其他数多。
算法:  
Boyer-Moore 算法的本质和方法四中的分治十分类似。我们首先给出 Boyer-Moore 算法的详细步骤：  
我们维护一个候选众数 candidate 和它出现的次数 count。初始时 candidate 可以为任意值，count 为 0；  
我们遍历数组 nums 中的所有元素，对于每个元素 x，在判断 x 之前，如果 count 的值为 0，我们先将 x 的值赋予 candidate，随后我们判断 x：  
如果 x 与 candidate 相等，那么计数器 count 的值增加 1；  
如果 x 与 candidate 不等，那么计数器 count 的值减少 1。  
在遍历完成后，candidate 即为整个数组的众数。











