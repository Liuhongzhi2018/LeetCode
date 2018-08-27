#  Permutation Sequence

## 问题分析
The set [1,2,3,...,n] contains a total of n! unique permutations.

Given n and k, return the kth permutation sequence.

给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

给定 n 和 k，返回第 k 个排列。

## 代码实现
``` C++
class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> nums(n);
        int i,j,sel,cnt = 1;
        for(i = 0; i < n; ++i) {
            nums[i] = i + 1;
            cnt *= (i + 1);
        }
        k--;
		string res = "";
        for(i = 0 ; i < n; i++) {
			cnt = cnt/(n-i);
            sel = k / cnt;
			res += ('0' + nums[sel]);
            for(j = sel; j < n-i-1; j++)
                nums[j] = nums[j+1];
            k = k % cnt;
        }
        return res;
    }
};
```

## 总结体会

本题要求根据给定的自然数集合中得到n的阶乘个数的排列，然后返回所有排列中给定的第k个排列。

在算法设计上，首先定义cnt变量赋予阶乘值；其次sel变量保存该组排列的第一个元素值，然后依次求出第2个到第n个元素；最后字符串res保存所求的第k个排列。
