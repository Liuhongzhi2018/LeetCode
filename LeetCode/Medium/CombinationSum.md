#  Combination Sum

## 问题分析

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

## 代码实现

1.
``` C++
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int> > ans;
        vector<int> out;
        sort(candidates.begin(), candidates.end());
        recursion(candidates, target, 0, out, ans);
        return ans;
    }
    void recursion(vector<int> &candidates, int target, int start, vector<int> &out, vector<vector<int> > &res) {
        int i;
        if (target < 0) return;
        else if (target == 0) res.push_back(out);
        else {
            for (i = start; i < candidates.size(); i++) {
                out.push_back(candidates[i]);
                recursion(candidates, target - candidates[i], i, out, res);
                out.pop_back();
            }
        }
    }
};
```

2.
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        self.res = []
        def recursive(idx,targ,cur):
            for i in range(idx,len(nums)):
                ni = nums[i]
                if ni<targ:
                    recursive(i,(targ-ni),cur+[ni])
                else:
                    if ni==targ:
                        self.res.append(cur+[ni])
                    break
        recursive(0,target,[])
        return self.res
```

3.
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        newcond = sorted(candidates)
        ans = []

        def find(s, use, remain):
            for i in range(s, len(newcond)):
                c = newcond[i]
                if c == remain:
                    ans.append(use+[c])
                if c < remain:
                    find(i, use+[c], remain-c)
                if c> remain:
                    return

        find(0, [], target)

        return ans
```

4.回溯法
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i, tmp_sum, tmp):
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                backtrack(j, tmp_sum+candidates[j],tmp+[candidates[j]])
        
        backtrack(0, 0, [])
        return res
```

## 总结体会

本题要求从无重复元素数组中找出满足和等于target的组合形式，这种组合既可以1个数，也可以多个数构成。

在算法设计上，首先用sort函数对数组进行重排；其次调用recursion递归函数求得所有组合情况，out为组合中的一个，ans为所有组合情况，每得到一个组合，target从数组中去掉已经找到的元素；最后ans返回即为满足要求的组合。

首先给数组进行一次排序，初始化self.res，声明recursive function递归函数，遍历下标如果当前比target小则继续迭代；最后递归0，target和一个空列表即可完成递归。

回溯法模板，实回溯算法关键在于:不合适就退回上一步，然后通过约束条件, 减少时间复杂度.