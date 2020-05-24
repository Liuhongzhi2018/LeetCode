#  Group Anagrams

## 问题分析

Given an array of strings, group anagrams together.

给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

## 代码实现

1.
``` C++
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>>corres;
        int i=0;
        for(auto s:strs){
            sort(s.begin(),s.end());
            corres[s].push_back(strs[i++]);
        }
        vector<vector<string>>res;
        for(auto n:corres){
            sort(n.second.begin(),n.second.end());
            res.push_back(n.second);
        }
        return res;
    }
};
```

2.
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_ = {}
        for i in range(len(strs)):
            tmp = ''.join(sorted(strs[i]))
            if tmp in map_:
                map_[tmp].append(strs[i])
            else:
                map_[tmp] = [strs[i]]
        return [v for v in map_.values()]
```

## 总结体会

本题要求从字符串数组中找出满足字母异位词条件的单词，并放在同一个一维数组中。

在算法设计上，首先将字符串进行排序排序，利用STL的map容器将每一个字符串排序后作为key，则value就保存所有具有相同字母的字符串；其次遍历一遍就把字符串保存在了map中；最后对排过序的集合输出到二维向量res中，返回即为所求的字母异位词组合。

思路：处理过程用map进行保存；key和value值分别对应 字母的从小到大排列值 和 strs中的真实值。