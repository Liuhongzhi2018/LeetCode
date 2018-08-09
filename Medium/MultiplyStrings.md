#  Multiply Strings

## 问题分析
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

## 代码实现
``` C++
class Solution {
public:
    string multiply(string num1, string num2) {
        string eql;
        int i,j;
        int n1 = num1.size(), n2 = num2.size();
        int k = n1 + n2 - 2, carry = 0;
        vector<int> loc(n1 + n2, 0);
        for (i = 0; i < n1; i++) {
            for (j = 0; j < n2; j++) {
                loc[k - i - j] += (num1[i] - '0') * (num2[j] - '0');
            }
        }
        for (i = 0; i < n1 + n2;i ++) {
            loc[i] += carry;
            carry = loc[i] / 10;
            loc[i] %= 10;
        }
        i = n1 + n2 - 1;
        while (loc[i] == 0)   i--;
        if (i < 0)   return "0";
        while (i >= 0)   eql.push_back(loc[i--] + '0');
        return eql;
    }
};
```

## 总结体会

本题要求对字符串的数字进行乘法运算，得到字符串形式的乘积结果。

在算法设计上，首先声明一维数组loc，保存错位相乘再相加的结果；然后用for循环加上各位的进位；最后去除首位0返回的字符串eql即是所求的乘积结果。
