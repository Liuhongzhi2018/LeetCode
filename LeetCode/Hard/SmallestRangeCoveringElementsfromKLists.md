#   Smallest Range Covering Elements from K Lists

## 问题描述

You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

你有 k 个升序排列的整数列表。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。

我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

## 代码实现

1.双指针方法
```python
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        indices = collections.defaultdict(list)
        xMin, xMax = 10**9, -10**9
        for i, vec in enumerate(nums):
            for x in vec:
                indices[x].append(i)
            xMin = min(xMin, *vec)
            xMax = max(xMax, *vec)
        
        freq = [0] * n
        inside = 0
        left, right = xMin, xMin - 1
        bestLeft, bestRight = xMin, xMax

        while right < xMax:
            right += 1
            if right in indices:
                for x in indices[right]:
                    freq[x] += 1
                    if freq[x] == 1:
                        inside += 1
                while inside == n:
                    if right - left < bestRight - bestLeft:
                        bestLeft, bestRight = left, right
                    if left in indices:
                        for x in indices[left]:
                            freq[x] -= 1
                            if freq[x] == 0:
                                inside -= 1
                    left += 1

        return [bestLeft, bestRight]
```

2.堆方法
```python
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        rangeLeft, rangeRight = -10**9, 10**9 
        maxValue = max(vec[0] for vec in nums) 
        priorityQueue = [(vec[0], i, 0) for i, vec in enumerate(nums)] 
        heapq.heapify(priorityQueue) 
        
        while True: 
            minValue, row, idx = heapq.heappop(priorityQueue)
            if maxValue - minValue < rangeRight - rangeLeft:
                rangeLeft, rangeRight = minValue, maxValue
            if idx == len(nums[row]) - 1: 
                break 
            maxValue = max(maxValue, nums[row][idx + 1])
            heapq.heappush(priorityQueue, (nums[row][idx + 1], row, idx + 1)) 
        return [rangeLeft, rangeRight]
```


## 思路总结

1. 双指针方法  
在讲这个方法之前我们先思考这样一个问题：有一个序列 A={a1,a2,⋯ ,an} 和一个序列 B={b1,b2,⋯ ,bm}，请找出一个 B 中的一个最小的区间，使得在这个区间中 A 序列的每个数字至少出现一次，请注意 A 中的元素可能重复，也就是说如果 A 中有 p 个 u，那么你选择的这个区间中 u 的个数一定不少于 p。没错，这就是我们五月份的一道打卡题：「76. 最小覆盖子串」。官方题解使用了一种双指针的方法，遍历整个 BBB 序列并用一个哈希表表示当前窗口中的元素：  
    右边界在每次遍历到新元素的时候右移，同时将拓展到的新元素加入哈希表  
    左边界右移当且仅当当前区间为一个合法的答案区间，即当前窗口内的元素包含 A 中所有的元素，同时将原来左边界指向的元素从哈希表中移除  
    答案更新当且仅当当前窗口内的元素包含 A 中所有的元素
    
回到这道题，我们发现这两道题的相似之处在于都要求我们找到某个符合条件的最小区间，我们可以借鉴「76. 最小覆盖子串」的做法：这里序列 {0,1,⋯ ,k−1} 就是上面描述的 A 序列，即 k 个列表，我们需要在一个 B 序列当中找到一个区间，可以覆盖 A 序列。这里的 B 序列是什么？我们可以用一个哈希映射来表示 B 序列—— B[i] 表示 i 在哪些列表当中出现过，这里哈希映射的键是一个整数，表示列表中的某个数值，哈希映射的值是一个数组，这个数组里的元素代表当前的键出现在哪些列表里。

2. 堆方法  
给定 k 个列表，需要找到最小区间，使得每个列表都至少有一个数在该区间中。该问题可以转化为，从 k 个列表中各取一个数，使得这 k 个数中的最大值与最小值的差最小。

假设这 k 个数中的最小值是第 i 个列表中的 x，对于任意 j≠i，设第 j 个列表中被选为 k 个数之一的数是 y，则为了找到最小区间，y 应该取第 j 个列表中大于等于 x 的最小的数。简单证明如下：假设 z 也是第 j 个列表中的数，且 z>y，则有 z−x>y−x，同时包含 x 和 z 的区间一定不会小于同时包含 x 和 y 的区间。因此，其余 k−1 个列表中应该取大于等于 x 的最小的数。

由于 k 个列表都是升序排列的，因此对每个列表维护一个指针，通过指针得到列表中的元素，指针右移之后指向的元素一定大于或等于之前的元素。

使用最小堆维护 k 个指针指向的元素中的最小值，同时维护堆中元素的最大值。初始时，k 个指针都指向下标 0，最大元素即为所有列表的下标 0 位置的元素中的最大值。每次从堆中取出最小值，根据最大值和最小值计算当前区间，如果当前区间小于最小区间则用当前区间更新最小区间，然后将对应列表的指针右移，将新元素加入堆中，并更新堆中元素的最大值。

如果一个列表的指针超出该列表的下标范围，则说明该列表中的所有元素都被遍历过，堆中不会再有该列表中的元素，因此退出循环。
