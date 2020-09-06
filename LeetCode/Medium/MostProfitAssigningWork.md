#  Most Profit Assigning Work

## 问题描述

We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job. 

Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i]. 

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

有一些工作：difficulty[i] 表示第 i 个工作的难度，profit[i] 表示第 i 个工作的收益。

现在我们有一些工人。worker[i] 是第 i 个工人的能力，即该工人只能完成难度小于等于 worker[i] 的工作。

每一个工人都最多只能安排一个工作，但是一个工作可以完成多次。

举个例子，如果 3 个工人都尝试完成一份报酬为 1 的同样工作，那么总收益为 $3。如果一个工人不能完成任何工作，他的收益为 $0 。

我们能得到的最大收益是多少？


## 代码实现

1.
```python
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = list(zip(difficulty, profit)) 
        jobs.sort() 
        ans = i = best = 0 
        for skill in sorted(worker): 
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1]) 
                i += 1
                
            ans += best
        return ans
```


## 思路总结

双指针方法：我们可以以任意顺序考虑工人，所以我们按照能力大小排序。  
如果我们先访问低难度的工作，那么收益一定是截至目前最好的。  
我们使用 “双指针” 的方法去安排任务。我们记录最大可用利润 best。对于每个能力值为 skill 的工人，找到难度小于等于能力值的任务，并将如结果中。