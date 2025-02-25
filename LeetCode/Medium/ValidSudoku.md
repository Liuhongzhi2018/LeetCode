#  Valid Sudoku

## 问题分析

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules: Each row must contain the digits 1-9 without repetition; Each column must contain the digits 1-9 without repetition; Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。数字 1-9 在每一行只能出现一次;数字 1-9 在每一列只能出现一次;数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

## 代码实现

1.
``` C++
class Solution {
public:
    bool isValidSudoku(vector<vector<char> > &board) {
		int i,j,num;
        vector<vector<bool>> horizontal(9, vector<bool>(9,false));
		vector<vector<bool>> vertical(9, vector<bool>(9,false));
		vector<vector<bool>> square(9, vector<bool>(9,false));
		for(i = 0; i < 9; i++)
			for(j = 0; j < 9; j++){
				if(board[i][j] == '.')   continue;
				num = board[i][j] - '1';
				if(horizontal[i][num] || vertical[j][num] || square[i - i%3 + j/3][num])   return false;
				horizontal[i][num] = vertical[j][num] = square[i - i%3 + j/3][num] = true;
			}
	return true;
    }
};
```

2.
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sets = {}
        for i in range(9):
            for j in range(9):
                d = board[i][j]
                if d=='.':
                    continue
                z = (j//3)*3+(i//3)
                if (z,d) in sets or (0,i,d) in sets \
                or (1,j,d) in sets:
                    return False
                sets[(z,d)] = 1
                sets[(0,i,d)] = 1
                sets[(1,j,d)] = 1
        return True
```

## 总结体会

本题要求判断所给数独是否满足要求，即在每一个九宫格内不出现重复数字。

在算法设计上，采用for循环嵌套，首先判断行，再判断列，最后判断九宫格，不出现重复数字，即满足有效数独的题目要求。

首先定一个大容器字典，然后在字典里面存每一行，每一列，每一个3x3宫格出现过的数字，如果再出现则直接返回False，否则存放在相应的3x3宫格中。其中0和1是用于区分行和列位置。