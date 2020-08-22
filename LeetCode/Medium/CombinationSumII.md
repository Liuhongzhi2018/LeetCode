#  CombinationSumII

## 问题分析

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

## 代码实现

1.
``` C++
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        if(target==0) return{};
        set<vector<int>> com;
        vector<int> cond;
        sort(candidates.begin(), candidates.end());
        combinationSum2(candidates, target, 0, cond, com);
        return vector<vector<int>>(com.begin(), com.end());
    }
    void combinationSum2(vector<int>& candidates, int target, int idx, vector<int> &cond, set<vector<int>>& com){
        int i;
        if(target<0) return;
        else if (target==0) {
            com.insert(cond);
            return;
        }
        for(i = idx; i<candidates.size(); i++){
            cond.push_back(candidates[i]);
            combinationSum2(candidates, target-candidates[i], i+1, cond, com);
            cond.pop_back();
        }
    }
};
```

2.
```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        self.res = []
        def recursive(idx,targ,cur):
            for i in range(idx,len(candidates)):
                ni = nums[i]
                if ni<targ:
                    if i==idx or ni!=nums[i-1]:
                        recursive(i+1,(targ-ni),cur+[ni])
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
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0 or len(candidates) == 0:
            return []
        res = []
        candidates.sort()

        def backtrack(tar, idx, cur):
            if tar == 0:
                res.append(cur[:])
                return
            for i in range(idx, len(candidates)):
                if candidates[i] > tar:
                    break
                # 剪枝
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                cur.append(candidates[i])
                backtrack(tar-candidates[i], i+1, cur)
                cur.pop()

        backtrack(target, 0, [])
        return res
```

## 总结体会

本题与上一题的区别在于，给定数组candidates中含有重复数字，并且要求在组合中每个数字只能使用一次，

在算法设计上，首先声明set容器存储各不相同的组合情况和vector容器返回每一种组合；其次对给定数组进行顺序重排，然后运用递归算法并调用函数求得每一种组合；最后将所有组合情况返回。

在迭代时除了更新new target外，下标也要+1，因为不能使用重复元素。注意迭代时的条件设置。