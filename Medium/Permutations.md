#  Permutations

## 问题分析
Given a collection of distinct integers, return all possible permutations.

给定一个没有重复数字的序列，返回其所有可能的全排列。

## 代码实现
``` C++
class Solution {
public:
    vector<vector<int> > permute(vector<int> &num)
    {
        int i,j;
        vector<vector<int> > ret;
        if (num.size() < 2) {
            ret.push_back(num);
            return ret;
        }
        vector<vector<int> > post;
        vector<int> tmp;
        vector<int> cur;
        for (i = 0; i < num.size(); i++)
        {
            tmp = num;
            tmp.erase(tmp.begin() + i);
            post = permute(tmp);
            for (j = 0; j < post.size(); j++)
            {
                cur = post[j];
                cur.insert(cur.begin(), num[i]);
                ret.push_back(cur);
            }
        }
        return ret;
    }
};
```

## 总结体会

本题要求根据所给的数字序列，求出所有的全排列情况，并用向量ret返回。

在算法设计上，首先声明二维向量ret用于返回结果，如果序列为空或者只有一个元素则直接返回ret； 其次遍历数字序列中的元素，找到组合情况，然后把num中相应位置的数去掉，其余数字结果保存在二维向量post中；最后所有组合情况用ret返回即为所求。
