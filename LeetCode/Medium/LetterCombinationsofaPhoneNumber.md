#  Letter Combinations of a Phone Number

## 问题分析
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

## 代码实现
1.
``` C++
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> com;
        if (digits.empty()) return com;
        string ditstr[] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        traverse(digits, ditstr, 0, "", com);
        return com;
    }
    void traverse(string digits, string dis[], int gen, string out, vector<string> &ret) {
        int i;
        if (gen == digits.size()) ret.push_back(out);
        else {
            string str = dis[digits[gen] - '2'];
            for (i = 0; i < str.size(); i++) {
                out.push_back(str[i]);
                traverse(digits, dis, gen + 1, out, ret);
                out.pop_back();
            }
        }
    }
};
```

2.
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num2c = {
            "2":"abc","3":"def","4":"ghi",
            "5":"jkl","6":"mno","7":"pqrs",
            "8":"tuv","9":"wxyz",
        }
        if len(digits)==0 or '1' in digits:
            return []
        res = ['']
        for i in digits:
            res = [k+j for k in res for j in num2c[i]]
        return res
```

## 总结体会

本题要求从给出的电话数字中，得到所有字母的排列组合方式。

算法设计上，首先声明一个字符串保存所有电话上的数字与字母的对应组合，其次调用递归函数traverse，遍历所给数组中的数字；最后将所得到的字符串组合ret返回到letterCombinations函数，com字符串返回即为所求。



