#  Perfect Squares

## 问题描述

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

## 代码实现

1.动态规划
```python
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        dp = [float('inf')] *(n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square]+1)

        return dp[-1]
```

2.贪心枚举
```python
class Solution:
    def numSquares(self, n: int) -> int:

        def is_divided_by(n, count):
            if count == 1:
                return n in square_nums
        
            for k in square_nums:
                if is_divided_by(n-k, count-1):
                    return True
            return False

        square_nums = set([i*i for i in range(1, int(n**0.5)+1)])

        for count in range(1, n+1):
            if is_divided_by(n, count):
                return count
```

3.贪心 + BFS（广度优先搜索）
```python
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i * i for i in range(1, int(n**0.5)+1)] 
        level = 0 
        queue = {n} 
        while queue: 
            level += 1 
            next_queue = set() 
            for remainder in queue: 
                for square_num in square_nums: 
                    if remainder == square_num: 
                        return level 
                    elif remainder < square_num: 
                        break 
                    else: next_queue.add(remainder - square_num) 
            queue = next_queue 
        return level
```

4.数学运算
```python
class Solution:
    def isSquare(self, n: int) -> bool:
        sq = int(math.sqrt(n))
        return sq*sq == n

    def numSquares(self, n: int) -> int:
        while (n & 3) == 0: 
            n >>= 2 
        if (n & 7) == 7: 
            return 4 
        
        if self.isSquare(n): 
            return 1 
        for i in range(1, int(n**(0.5)) + 1): 
            if self.isSquare(n - i*i): 
                return 2
        return 3
```


## 思考总结

动态规划: 使用暴力枚举法会超出时间限制的原因很简单，因为我们重复的计算了中间解。我们以前的公式仍然是有效的。我们只需要一个更好的方法实现这个公式。  
numSquares(n)=min⁡(numSquares(n-k) + 1)   ∀k∈square   
你可能注意到从公式看来，这个问题和斐波那契数问题类似。和斐波那契数一样，我们由几种更有效的方法来计算解，而不是简单的递归。  
解决递归中堆栈溢出的问题的一个思路就是使用动态规划（DP）技术，该技术建立在重用中间解的结果来计算终解的思想之上。  
要计算 numSquares(n)的值，首先要计算n之前的所有值，即 numSquares(n−k)∀k∈square。如果我们已经在某个地方保留了数字 n−k 的解，那么就不需要使用递归计算。

贪心枚举：递归解决方法为我们理解问题提供了简洁直观的方法。我们仍然可以用递归解决这个问题。为了改进上述暴力枚举解决方案，我们可以在递归中加入贪心。我们可以将枚举重新格式化如下：  
从一个数字到多个数字的组合开始，一旦我们找到一个可以组合成给定数字 n 的组合，那么我们可以说我们找到了最小的组合，因为我们贪心的从小到大的枚举组合。  
为了更好的解释，我们首先定义一个名为 is_divided_by(n, count) 的函数，该函数返回一个布尔值，表示数字 n 是否可以被一个数字 count 组合，而不是像前面函数 numSquares(n) 返回组合的确切大小。

贪心 + BFS（广度优先搜索），正如上述贪心算法的复杂性分析种提到的，调用堆栈的轨迹形成一颗 N 元树，其中每个结点代表 is_divided_by(n, count) 函数的调用。基于上述想法，我们可以把原来的问题重新表述如下：
给定一个 N 元树，其中每个节点表示数字 n 的余数减去一个完全平方数的组合，我们的任务是在树中找到一个节点，该节点满足两个条件：
(1) 节点的值（即余数）也是一个完全平方数。
(2) 在满足条件（1）的所有节点中，节点和根之间的距离应该最小。

数学运算，随着时间的推移，已经提出并证明的数学定理可以解决这个问题。在这一节中，我们将把这个问题分成几个例子。  
1770 年，Joseph Louis Lagrange证明了一个定理，称为四平方和定理，也称为 Bachet 猜想，它指出每个自然数都可以表示为四个整数平方和：
p=a0^2+a1^2+a2^2+a3^2，其中 a0,a1,a2,a3表示整数。

python3最基础的BFS套路代码:  
BFS 其实是很简单的基础算法，抓住如下几点即可轻松写出不易错的 baseline:  
BFS 算法组成的 3 元素：队列，入队出队的节点，已访问的集合。  
    队列：先入先出的容器；  
    节点：最好写成单独的类，比如本例写成 (value,step) 元组。也可写成 (value,visited)，看自己喜好和题目；  
    已访问集合：为了避免队列中插入重复的值  
    
BFS算法组成的套路：  
    初始化三元素：  
    Node = node(n) queue = [Node] visited = set([Node.value])  
    操作队列 —— 弹出队首节点：  
    vertex = queue.pop(0)
    操作弹出的节点 —— 根据业务生成子节点（一个或多个）：  
    [node(vertex.value - n*n, Node.step+1) for n in range(1,int(vertex.value**.5)+1)]
    判断这些节点 —— 符合业务条件，则return，不符合业务条件，且不在已访问集合，则追加到队尾，并加入已访问集合：

if i==0:                     
    return new_vertex.step  
            
elif i not in visited:  
    queue.append(new_vertex)  
    visited.add(i)

若以上遍历完成仍未return，下面操作返回未找到代码：
return -1
