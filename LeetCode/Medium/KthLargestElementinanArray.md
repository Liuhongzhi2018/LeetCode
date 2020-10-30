#  Kth Largest Element in an Array

## 问题分析

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

## 代码实现

1. 先排序再返回指定大小的元素
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x: x)
        return nums[-k]
```

2.
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.nlargest(k, nums)  [6,5]
        return heapq.nlargest(k, nums)[-1]
```

3.
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq 
        heap = [] 
        heapify(heap) 
        for num in nums: 
            heappush(heap, num) 
            if len(heap) > k: 
                heappop(heap) 
        return heap[0]
```


## 总结体会

heapq.nlargest(n, iterable, key=None)
从 iterable 所定义的数据集中返回前 n 个最大元素组成的列表。 如果提供了 key 则其应指定一个单参数的函数，用于从 iterable 的每个元素中提取比较键 (例如 key=str.lower)。 等价于: sorted(iterable, key=key, reverse=True)[:n]。

heapq.nsmallest(n, iterable, key=None)
从 iterable 所定义的数据集中返回前 n 个最小元素组成的列表。 如果提供了 key 则其应指定一个单参数的函数，用于从 iterable 的每个元素中提取比较键 (例如 key=str.lower)。 等价于: sorted(iterable, key=key)[:n]。
