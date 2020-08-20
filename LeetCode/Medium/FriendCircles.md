#  Friend Circles

## 问题描述

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。


## 代码实现

1.BFS广度优先搜索
```python
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def BFS(M,q,visited):
            while q:
                i = q.pop(0)
                visited[i] = 1
                for j in range(len(M)):
                    if M[i][j] == 1 and visited[j] == 0:
                        q.append(j)
                        visited[j] = 1
        
        n = len(M)
        q = []
        visited = [0] * n
        count = 0
        for i in range(n):
            if visited[i] == 0:
                q.append(i)
                BFS(M, q, visited)
                count += 1
        return count
```

2.DFS深度优先搜索
```python
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def DFS(M, i, visited):
            visited[i] = 1
            for j in range(len(M)):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    DFS(M, j, visited)
        
        n = len(M)
        visited = [0] * n
        count = 0
        for i in range(n):
            if visited[i] == 0:
                DFS(M, i, visited)
                count += 1
        return count
```

3.同一朋友圈的ID编号设置为相同
```python
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        relation = list(range(n))
        def connect(i,j,relationList):
            t = relationList[j]
            s = relationList[i]
            for i in range(len(relationList)):
                if relationList[i] == t:
                    relationList[i] = s
        for i in range(n):
            for j in range(n):
                if j < i and M[i][j] == 1:
                    connect(j, i, relation)
        return len(set(relation))
```


## 思路总结

深度优先搜索：给定的矩阵可以看成图的邻接矩阵。这样我们的问题可以变成无向图连通块的个数。

广度优先搜索：上面的算法中提到，如果我们把矩阵看成图的邻接矩阵，我们可以使用图算法很快的算出连通块的个数。这可以用到图中的广度优先搜索。在广度优先搜索中，我们从一个特定点开始，访问所有邻接的节点。然后对于这些邻接节点，我们依然通过访问邻接节点的方式，知道访问所有可以到达的节点。因此，我们按照一层一层的方式访问节点。

并查集：另一种统计图中连通块数量的方法是使用并查集。方法很简单。
使用一个大小为 N 的 parent 数组，遍历这个图，每个节点我们都遍历所有相邻点，并让相邻点指向它，并设置成一个由 parent 节点决定的单独组。这个过程被称为 union。这样每个组都有一个唯一的 parent 节点，这些节点的父亲为 -1。
对于每对新节点，我们找寻他们的父亲。如果父亲节点一样，那么什么都不做他们已经是一个组里。如果父亲不同，说明他们仍然需要合并。因此，将他们的父亲合并，也就是 parent[parent[x]]=parent[y]，这样就让他们在一个组里了。