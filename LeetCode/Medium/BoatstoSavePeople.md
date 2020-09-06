#   Boats to Save People

## 问题描述

The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回载到每一个人所需的最小船数。(保证每个人都能被船载)。



## 代码实现

1.双指针
```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() 
        i, j = 0, len(people) - 1 
        ans = 0 
        while i <= j: 
            ans += 1 
            if people[i] + people[j] <= limit: 
                i += 1 
            j -= 1 
        return ans
```


## 思路总结

贪心（双指针）方法  
思路  
如果最重的人可以与最轻的人共用一艘船，那么就这样安排。否则，最重的人无法与任何人配对，那么他们将自己独自乘一艘船。  
这么做的原因是，如果最轻的人可以与任何人配对，那么他们也可以与最重的人配对。

算法  
令 people[i] 指向当前最轻的人，而 people[j] 指向最重的那位。  
然后，如上所述，如果最重的人可以与最轻的人共用一条船（即 people[j] + people[i] <= limit），那么就这样做；否则，最重的人自己独自坐在船上。