#  Permutations

## 问题描述

Given a collection of distinct integers, return all possible permutations.

给定一个没有重复数字的序列，返回其所有可能的全排列。

## 代码实现

1.
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

2.递归法
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        self.res = []
        def recursion(path, cand):
            if len(cand) == 0:
                self.res.append(path)
            for i, n in enumerate(cand):
                recursion(path+[n],cand[:i]+cand[i+1:])
        recursion([],nums)
        return self.res

```

3.搜索回溯法
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first,n):
                # 动态维护数组 
                nums[first], nums[i] = nums[i], nums[first] 
                # 继续递归填下一个数 
                backtrack(first + 1) 
                # 撤销操作 
                nums[first], nums[i] = nums[i], nums[first]


        n = len(nums)
        res = []
        backtrack()
        return res
```

## 思考总结

本题要求根据所给的数字序列，求出所有的全排列情况，并用向量ret返回。

在算法设计上，首先声明二维向量ret用于返回结果，如果序列为空或者只有一个元素则直接返回ret； 其次遍历数字序列中的元素，找到组合情况，然后把num中相应位置的数去掉，其余数字结果保存在二维向量post中；最后所有组合情况用ret返回即为所求。

搜索回溯思路和算法  
这个问题可以看作有 nnn 个排列成一行的空格，我们需要从左往右依此填入题目给定的 nnn 个数，每个数只能使用一次。那么很直接的可以想到一种穷举的算法，即从左往右每一个位置都依此尝试填入一个数，看能不能填完这 nnn 个空格，在程序中我们可以用「回溯法」来模拟这个过程。

如果 first<n，我们要考虑这第 first 个位置我们要填哪个数。根据题目要求我们肯定不能填已经填过的数，因此很容易想到的一个处理手段是我们定义一个标记数组 vis[] 来标记已经填过的数。使用标记数组来处理填过的数是一个很直观的思路，但是可不可以去掉这个标记数组呢？毕竟标记数组也增加了我们算法的空间复杂度。
答案是可以的，我们可以将题目给定的 n 个数的数组 nums[] 划分成左右两个部分，左边的表示已经填过的数，右边表示待填的数，我们在递归搜索的时候只要动态维护这个数组即可。

回溯算法的重点就是：怎么前进（进入下一个状态）； 怎么回退（回到上一个状态）； 再加上搞明白什么时候停止。 其中比较重要的是：采取何种方式处理好状态的前进和回退。在本题中，在前进时，需要查看当前数字是否已经在组合的路径中，也就是要回避非法状态；在回退时，要将当前数字从组合的路径中删除，以达到回溯、不影响进入到下一个状态的目的。 参考大佬的思路