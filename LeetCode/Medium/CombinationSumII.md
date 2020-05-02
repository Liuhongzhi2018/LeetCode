#  CombinationSumII

## 问题分析
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

## 代码实现
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

## 总结体会

本题与上一题的区别在于，给定数组candidates中含有重复数字，并且要求在组合中每个数字只能使用一次，

在算法设计上，首先声明set容器存储各不相同的组合情况和vector容器返回每一种组合；其次对给定数组进行顺序重排，然后运用递归算法并调用函数求得每一种组合；最后将所有组合情况返回。
