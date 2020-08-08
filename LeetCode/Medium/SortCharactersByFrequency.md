#  Sort Characters By Frequency

## 问题分析

Given a string, sort it in decreasing order based on the frequency of characters.

给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

## 代码实现

1. 字典排序
```python
class Solution:
    def frequencySort(self, s: str) -> str:
        sdict = {}
        for w in s:
            if w in sdict:
                sdict[w] += 1
            else:
                sdict[w] = 1
        newdict = sorted(sdict.items(),key=lambda x:x[1], reverse=True)
        news = ""
        for key, value in newdict:
            while value:
                news += key
                value -= 1
        return news
```

2. 大顶堆
```python
class Solution:
    def frequencySort(self, s: str) -> str:
        cf = collections.defaultdict(int)
        for i in s:
            cf[i] += 1
        slist = []
        heapq.heapify(slist)
        for i in cf:
            for j in range(cf[i]):
                heapq.heappush(slist,(-cf[i],i))

        return ''.join([heapq.heappop(slist)[1] for _ in range(len(s))])
```

3. 桶排序
```python
class Solution:
    def frequencySort(self, s: str) -> str:
        ret = []
        cf = collections.defaultdict(int)
        for i in s:
            cf[i] += 1
        buckets = [[] for _ in range(len(s)+1)]
        for i in cf:
            buckets[cf[i]].extend(i*cf[i])
        for i in buckets[::-1]:
            if i:
                ret.extend(i)
        return ''.join(ret)
```




## 总结体会

方法一是将列表元素按照元素和出现频率的键值对形式保存到字典中，并且按照value值进行从大到小排序，根据value值重复添加字母到字符串中，将得到的字符串返回。