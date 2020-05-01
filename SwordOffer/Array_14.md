# 数字在排序数组中出现的次数


## 题目描述

统计一个数字在排序数组中出现的次数。

## 代码实现

1. 内置函数
```python
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if len(data) == 0:
            return 0
        else:
            return data.count(k)
```
运行时间：27ms

占用内存：5856k


2. 二分查找法
```python
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        # write code here
        if len(data) == 0:
            return 0
        else:
            count, mid = 0, len(data) // 2
            if k > data[mid]:
                for i in range(mid + 1, len(data)):
                    if data[i] == k:
                        count += 1
                return count
            elif k < data[mid]:
                for i in range(mid - 1, -1, -1):
                    if data[i] == k:
                        count += 1
                return count
            else:
                count += 1
                for i in range(mid - 1, -1, -1):
                    if data[i] == k:
                        count += 1
                    else:
                        break
                for i in range(mid + 1, len(data)):
                    if data[i] == k:
                        count += 1
                    else:
                        break
                return count
```
运行时间：22ms

占用内存：5724k



## 思路总结


