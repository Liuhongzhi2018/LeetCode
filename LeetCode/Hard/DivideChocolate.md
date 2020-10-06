#   Divide Chocolate

## 问题描述

你有一大块巧克力，它由一些甜度不完全相同的小块组成。我们用数组 sweetness 来表示每一小块的甜度。

你打算和 K 名朋友一起分享这块巧克力，所以你需要将切割 K 次才能得到 K+1 块，每一块都由一些 连续 的小块组成。

为了表现出你的慷慨，你将会吃掉 总甜度最小 的一块，并将其余几块分给你的朋友们。

请找出一个最佳的切割策略，使得你所分得的巧克力 总甜度最大，并返回这个 最大总甜度。

## 代码实现

1.二分查找
```python
class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """
        left = min(sweetness) # 结果的最小值
        right = sum(sweetness)//(K + 1) # 结果的最大值
        while left <= right:
            mid = (left + right) // 2
            
            cnt = 0 # 用来记录当我分到的巧克力甜度为mid的时候，切的总块数
            tmp = 0 # 当前切的这块巧克力的总甜度
            for sweet in sweetness:
                if (tmp + sweet) > mid:
                    cnt += 1
                    tmp = 0
                else:
                    tmp += sweet
            
            if cnt < K + 1: # 需要切更多块
                right = mid - 1
            else:
                left = mid + 1
        
        return left
```


## 思路总结

答案落在的区间[min(sweetness), sum(sweetness)//(k + 1)]，  
然后用二分法不断缩小区间范围即可。