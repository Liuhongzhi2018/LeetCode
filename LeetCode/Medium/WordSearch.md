#  Word Search

## 问题描述

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。



## 代码实现

1.深度优先搜索（DFS）和回溯
``` python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 定义上下左右四个行走方向
        self.directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])

        # 标记先列后行
        mark = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    # 找到后将元素标记
                    mark[i][j] = 1
                    if self.backtrack(i, j, mark, board, word[1:]) == True:
                        return True
                    else:
                        mark[i][j] = 0
        return False

    def backtrack(self, i, j, mark, board, word):
        if len(word) == 0:
            return True
        
        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]

            if 0<= cur_i < len(board) and 0<= cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                if mark[cur_i][cur_j] == 1:
                    continue
                # 将元素标记为已使用
                mark[cur_i][cur_j] = 1
                if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
                    return True
                else:
                    # 回溯
                    mark[cur_i][cur_j] = 0
        return False
```


## 思路总结

使用深度优先搜索（DFS）和回溯的思想实现。关于判断元素是否使用过，我用了一个二维数组 mark 对使用过的元素做标记。
外层：遍历  
首先遍历 board 的所有元素，先找到和 word 第一个字母相同的元素，然后进入递归流程。假设这个元素的坐标为 (i, j)，进入递归流程前，先记得把该元素打上使用过的标记：mark[i][j] = 1

内层：递归
打完标记后进入递归流程。递归流程主要做了这么几件事：  
从 (i, j) 出发，朝它的上下左右试探，看看它周边的这四个元素是否能匹配 word 的下一个字母  
如果匹配到了：带着该元素继续进入下一个递归  
如果都匹配不到：返回 False  
当 word 的所有字母都完成匹配后，整个流程返回 True

几个注意点：递归时元素的坐标是否超过边界；回溯标记 mark[i][j] = 0以及 return 的时机
