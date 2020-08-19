#  Word Ladder

## 问题描述

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.

Note:  
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：  
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。

说明:  
如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。


## 代码实现

1.广度优先搜索
```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList) 
        q=[(beginWord,1)] 
        if endWord not in wordList: 
            return 0 
        
        while q: 
            node,level=q.pop(0) 
            if node == endWord: 
                return level 
                
            for i in range(len(node)): 
                for j in "abcdefghijklmnopqrstuvwxyz": 
                    new=node[:i]+j+node[i+1:] 
                    if new in wordList: 
                        q.append((new,level+1))
                        wordList.remove(new) 
        return 0
```

## 思考总结

想法  
利用广度优先搜索搜索从 beginWord 到 endWord 的路径。

算法  
对给定的 wordList 做预处理，找出所有的通用状态。将通用状态记录在字典中，键是通用状态，值是所有具有通用状态的单词。  
将包含 beginWord 和 1 的元组放入队列中，1 代表节点的层次。我们需要返回 endWord 的层次也就是从 beginWord 出发的最短距离。  
为了防止出现环，使用访问数组记录。  
当队列中有元素的时候，取出第一个元素，记为 current_word。  
找到 current_word 的所有通用状态，并检查这些通用状态是否存在其它单词的映射，这一步通过检查 all_combo_dict 来实现。  
从 all_combo_dict 获得的所有单词，都和 current_word 共有一个通用状态，所以都和 current_word 相连，因此将他们加入到队列中。  
对于新获得的所有单词，向队列中加入元素 (word, level + 1) 其中 level 是 current_word 的层次。
最终当你到达期望的单词，对应的层次就是最短变换序列的长度。
