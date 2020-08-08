#  Top K Frequent Elements

## 问题分析

Given a non-empty array of integers, return the k most frequent elements.

给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

## 代码实现

1. 字典排序
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = {}
        for i in nums:
            if i in numdict:
                numdict[i] += 1
            else:
                numdict[i] = 1
        maxk = sorted(numdict.items(),key=lambda x: x[1])[-k:]
        result = []
        for i in maxk:
            result.append(i[0])
        return result
```

2. 字典排序优化代码
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        res = sorted(dic.items(),key=lambda x:x[1], reverse=True)
        return list(map(lambda x:x[0], res))[:k]
```


3.
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        queue, res = [], []
        for i in dic:
            heapq.heappush(queue,(-dic[i],i))
        for i in range(k):
            tmp = heapq.heappop(queue)
            res.append(tmp[1])
        return res 
```


## 总结体会

方法一是将列表元素按照元素和出现频率的键值对形式保存到字典中，并且按照value值进行从小到大排序，并且取出现频率最高的k个元素；将元素的所有key保存到列表中。

方法二用堆来实现，这样时间复杂度就是nlogk了(python默认为小顶堆，所以压入堆中时要取负数)。