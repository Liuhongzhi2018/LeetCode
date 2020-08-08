#  Longest Word in Dictionary through Deleting


## 问题分析

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string. 

给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。



## 代码实现

1.sort和find
```python 
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        # 对字典d进行排序，第一关键字是长度降序，第二关键字是字符串本身字典序
        d.sort(key=lambda x: (-len(x), x))
        # 匹配函数
        def match(c):
            i = 0
            # 遍历字符串里的字母
            for j in c:
                # 查找函数，后一个参数是查找起点
                k = s.find(j,i)
                # 查找失败就返回错误
                if k == -1:
                    return False
                # 查找成功就更新查找起点
                i = k + 1
            return True
        # 遍历字符串列表
        for c in d:
            # 如果符合条件就输出
            if match(c):
                return c
        # 否则输出空串
        return ''
```

2.sort和find
```python
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))
        def f(c):
            i = 0
            for j in c:
                if (i := s.find(j, i)) == -1:
                    return True
                i += 1
        return next((c for c in d if not f(c)), '') 
```

3. sort和双指针
```python
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))
        for ds in d:
            ps = 0
            dslen = len(ds)
            for pd in range(dslen):
                tmp = s.find(ds[pd],ps)
                if tmp != -1:
                    ps = tmp + 1
                else:
                    break
            else:
                return ds
        return ''
```


## 总结体会

当待排序列表的元素由多字段构成时，可以通过sorted(iterable，key，reverse)的参数key来制定我们根据那个字段对列表元素进行排序。-len(x)表示按照字符串长度降序，x表示按照字母表顺序。

find方法str.find(str, beg=0, end=len(string))，beg是起始的索引。