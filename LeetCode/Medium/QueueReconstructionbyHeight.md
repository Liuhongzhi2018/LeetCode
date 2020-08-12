#  Queue Reconstruction by Height

## 问题分析

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。


## 代码实现

1.
``` python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if len(people) <= 1:
            return people
        people_down = sorted(people, key=lambda x:(-x[0], x[1]))
        new_queue = [people_down[0]]
        for i in people_down[1:]:
            new_queue.insert(i[1],i)
        return new_queue
```


## 总结体会

给定一群人的一个队列，要求重新排序。队列中每个人由一个整数对(h, k)表示，其中h是这个人的身高，k表示在新队列中要求排在这个人前面且身高大于或等于h的人数。注：队列排序即数值排序

更通俗一点就是：假设有一个队列，已知每个人的身高h和排在该人前面的更高或一样高的人数k，现在给你打乱顺序后的数组，要求恢复原来的队列。

考虑将这群人依次加入新队列中，加入时需符合k的要求。注意到，一个人的k值实际上与身高更矮的人的位置无关，所以如果身高比之更高的人已经排好队了，这个人加入这个新队列的位置就可以根据k值确定了。因此，身高较高的人应该先加入，我们先对队列按身高降序排序。此外，对于相同身高的人，k值较小的人位置在前，优先加入。
