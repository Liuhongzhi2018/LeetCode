#  Fruit Into Baskets

## 问题描述

In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

    Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
    Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

在一排树中，第 i 棵树产生 tree[i] 型的水果。
你可以从你选择的任何树开始，然后重复执行以下步骤：

    把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
    移动到当前树右侧的下一棵树。如果右边没有树，就停下来。

请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。

你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。

用这个程序你能收集的水果树的最大总量是多少？


## 代码实现

1.滑动窗口
```python
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ans = i = 0 
        count = collections.Counter() 
        for j, x in enumerate(tree): 
            count[x] += 1 
            while len(count) >= 3: 
                count[tree[i]] -= 1 
                if count[tree[i]] == 0: 
                    del count[tree[i]] 
                i += 1 
            ans = max(ans, j - i + 1) 
        return ans
```


## 思路总结

想法  
在方法 1中，我们希望找到最长的包含两种不同“类型”的子序列，我们称这样的子序列为合法的。  
假设我们考虑所有以下标 j 为结尾的合法子序列，那么一定有一个最小的开始下标 i：称之为 opt(j) = i。  
我们会发现这个 opt(j) 是一个单调递增的函数，这是因为所有合法子序列的子序列一定也是合法的。

算法  
模拟一个滑动窗口，维护变量 i 是最小的下标满足 [i, j] 是合法的子序列。  
维护 count 是序列中各种类型的个数，这使得我们可以很快知道子序列中是否含有 3 中类型。