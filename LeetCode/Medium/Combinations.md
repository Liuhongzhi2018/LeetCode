#  Combinations

## 问题描述

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.

给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。


## 代码实现

1.回溯法
``` python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, cur = []):
            if len(cur) == k:
                output.append(cur[:])

            for i in range(first, n+1):
                cur.append(i)
                backtrack(i+1,cur)
                cur.pop()

        output = []
        backtrack()
        return output
```



## 思路总结

回溯法
是一种通过遍历所有可能成员来寻找全部可行解的算法。若候选 不是 可行解 (或者至少不是 最后一个 解)，回溯法会在前一步进行一些修改以舍弃该候选，换而言之， 回溯并再次尝试。
这是一个回溯法函数，它将第一个添加到组合中的数和现有的组合作为参数。 
backtrack(first, curr)若组合完成- 添加到输出中。遍历从 first t到 n的所有整数。将整数 i 添加到现有组合 curr中。继续向组合中添加更多整数backtrack(i + 1, curr).将 i 从 curr中移除，实现回溯。