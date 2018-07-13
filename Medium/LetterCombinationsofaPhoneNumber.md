#  Letter Combinations of a Phone Number

## 问题分析
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

## 代码实现
``` C++
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> com;
        if (digits.empty()) return com;
        string ditstr[] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        letterCombinationsDFS(digits, ditstr, 0, "", com);
        return com;
    }
    void letterCombinationsDFS(string digits, string dict[], int level, string out, vector<string> &res) {
        int i;
        if (level == digits.size()) res.push_back(out);
        else {
            string str = dict[digits[level] - '2'];
            for (i = 0; i < str.size(); i++) {
                out.push_back(str[i]);
                letterCombinationsDFS(digits, dict, level + 1, out, res);
                out.pop_back();
            }
        }
    }
};
```

## 总结体会

本题要求从给出的电话数字中，得到所有字母的排列组合方式。

算法设计上，首先声明一个字符串保存所有电话上的字母组合，其次调用递归函数letterCombinationsDFS，将所得到的字符串res返回，将com字符串返回即为所求。



