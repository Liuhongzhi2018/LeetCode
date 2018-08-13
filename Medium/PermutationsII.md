#  Permutations II

## 问题分析
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

给定一个可包含重复数字的序列，返回所有不重复的全排列。

## 代码实现
``` C++
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int> > ret;
        vector<int> lookup;
        vector<int> sign(nums.size(), 0);
        if (nums.size() < 2) {
            ret.push_back(nums);
            return ret;
        }
        sort(nums.begin(), nums.end());
        permuteUniqueDFS(nums, 0, sign, lookup, ret);
        return ret;
    }
    void permuteUniqueDFS(vector<int> &nums, int level, vector<int> &sign, vector<int> &lookup, vector<vector<int> > &ret) {
        int i;
        if (level >= nums.size()) ret.push_back(lookup);
        else {
            for (i = 0; i < nums.size(); ++i) {
                if (sign[i] == 0) {
                    if (i > 0 && nums[i] == nums[i - 1] && sign[i - 1] == 0) continue;
                    sign[i] = 1;
                    lookup.push_back(nums[i]);
                    permuteUniqueDFS(nums, level + 1, sign, lookup, ret);
                    lookup.pop_back();
                    sign[i] = 0;
                }
            }
        }
    }
};
```

## 总结体会

本题同样要求全排列，但是与上一题求全排列的不同之处在于有重复数字情况下组合不能重复。

在算法设计上，首先声明二维向量ret用于返回结果，如果序列为空或者只有一个元素则直接返回ret； 其次对数字序列进行排序，可以使相同元素在位置相邻；在递归函数中要判断前面一个数和当前的数是否相等，如果相等说明前面的数必须已经使用，仅对应的标志位sign向量为1时元素才能使用，否则需要跳过，避免产生重复排列；最后所有组合情况用ret返回即为所求排列。
