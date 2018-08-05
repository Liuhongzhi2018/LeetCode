#  Combination Sum

## 问题分析
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

## 代码实现
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

## 总结体会

本题要求从无重复元素数组中找出满足和等于target的组合形式，这种组合既可以1个数，也可以多个数构成。

在算法设计上，首先用sort函数对数组进行重排；其次调用recursion递归函数求得所有组合情况，out为组合中的一个，ans为所有组合情况，每得到一个组合，target从数组中去掉已经找到的元素；最后ans返回即为满足要求的组合。
