#  Letter Combinations of a Phone Number

## 问题描述

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

3.回溯法
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'], 
        '3': ['d', 'e', 'f'], 
        '4': ['g', 'h', 'i'], 
        '5': ['j', 'k', 'l'], 
        '6': ['m', 'n', 'o'], 
        '7': ['p', 'q', 'r', 's'], 
        '8': ['t', 'u', 'v'], 
        '9': ['w', 'x', 'y', 'z']} 
        
        def backtrack(combination, next_digits): # if there is no more digits to check 
            if len(next_digits) == 0: 
                # the combination is done 
                output.append(combination) 
            # if there are still digits to check 
            else: 
                # iterate over all letters which map 
                # the next available digit 
                for letter in phone[next_digits[0]]: 
                    # append the current letter to the combination 
                    # and proceed to the next digits 
                    backtrack(combination + letter, next_digits[1:]) 
        output = [] 
        if digits:
            backtrack("",digits)
        return output
```

## 思考总结

本题要求从给出的电话数字中，得到所有字母的排列组合方式。

算法设计上，首先声明一个字符串保存所有电话上的数字与字母的对应组合，其次调用递归函数traverse，遍历所给数组中的数字；最后将所得到的字符串组合ret返回到letterCombinations函数，com字符串返回即为所求。


方法二思路，首先用字典将数字映射到对应的字母；然后遍历在digits里面的所有数字，嵌套的for循环只用一行来表示。

方法三是回溯法。回溯是一种通过穷举所有可能情况来找到所有解的算法。如果一个候选解最后被发现并不是可行解，回溯算法会舍弃它，并在前面的一些步骤做出一些修改，并重新尝试找到可行解。  
给出如下回溯函数 backtrack(combination, next_digits) ，它将一个目前已经产生的组合 combination 和接下来准备要输入的数字 next_digits 作为参数。  
如果没有更多的数字需要被输入，那意味着当前的组合已经产生好了。
如果还有数字需要被输入：遍历下一个数字所对应的所有映射的字母。将当前的字母添加到组合最后，也就是 combination = combination + letter 。
重复这个过程，输入剩下的数字： backtrack(combination + letter, next_digits[1:]) 。