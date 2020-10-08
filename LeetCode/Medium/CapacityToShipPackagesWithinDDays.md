#  Capacity To Ship Packages Within D Days

## 问题描述

A conveyor belt has packages that must be shipped from one port to another within D days.

The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。


## 代码实现

1.二分查找
```python
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        low, high = max(weights), sum(weights)
        while low < high:
            mid = low + (high - low)//2
            days = self.need_days(weights, mid)
            if days <= D:
                high = mid
            else:
                low = mid + 1
        return low

    def need_days(self, weights, capacity):
        cnt = sums = 0
        for w in weights:
            sums += w
            if sums > capacity:
                cnt += 1
                sums = w
        return cnt + int(sums>0)
```


## 思路总结
 
1. 求解给定天数要完成时候的最低运载能力，可以转化二分遍历所有可能的运载能力，看看最小的可以在给定天数完成的运载能力是多少；最小、最大的运载能力分别为max(weights), sum(weights), 当给定最小运载能力时，可以很容易的得到需要多少天才能完成装载；
2. 在区间中二分查找运载能力即可，注意：当此时运载能力需要的天数小于等于给定天数时，右区间边界high=mid, 而不是high=mid-1，因为mid此时可能就是目标解（原则2缩减不能排除潜在答案），当等于给定天数时这一点很好理解，当小于时也需要设置high=mid。
举个例子，weights=[1,2,1,2], D=3, 开始low,high=2, 6, 此时mid=4, 发现需要天数为2, 小于D, 令high=4, 此时mid=3, 发现需要天数为2, 仍然小于D, 如果此时high=mid-1=2, 那么需要的天数就为4，错失了3这一个目标解。