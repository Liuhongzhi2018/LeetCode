#  Simplify Path

## 问题分析
Given an absolute path for a file (Unix-style), simplify it.

给定一个文档 (Unix-style) 的完全路径，请进行路径简化。

## 代码实现
``` C++
class Solution {
public:
    string simplifyPath(string path) {
        vector<string> point;
        int i = 0,start,end;
        string s,ret;
        while (i < path.size()) {
            while (path[i] == '/' && i < path.size()) i++;
            if (i == path.size()) break;
            start = i;
            while (path[i] != '/' && i < path.size()) i++;
            end = i - 1;
            s = path.substr(start, end - start + 1);
            if (s == "..") {
              if (!point.empty())  point.pop_back(); }
              else if (s != ".")  point.push_back(s);
        }
        if (point.empty()) return "/";
        for (i = 0; i < point.size(); i++)  ret += '/' + point[i];
        return ret;
    }
};
```

## 总结体会

本题要求将所给路径简化，主要是将路径看作"/"分割的字符串，将其中出现符合要求的中间字符串和符号删除。

在算法设计上，首先定义i遍历字符串，判断当前数组指向的字符是否需要简化；通过知道中间的"."和".."情况，删掉当前路径或者紧挨着的路径；最后将point向量保存的元素返回，即为简化后的路径。
