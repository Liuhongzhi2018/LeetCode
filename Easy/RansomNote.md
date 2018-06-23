#  Ransom Note

## 问题分析
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。

## 代码实现
``` C
bool canConstruct(char* ransomNote, char* magazine) {
    int i;
    int ranlen = strlen(ransomNote);
    int maglen = strlen(magazine);
    if (ranlen > maglen)  return false;
    int hash1[256] = { 0 };
    int hash2[256] = { 0 };
    for (i = 0; i<ranlen; i++)
        hash1[ransomNote[i]]++;
    for (i = 0; i<maglen; i++)
        hash2[magazine[i]]++;
    for (i = 0; i<256; i++){
        if (hash1[i] > hash2[i])  return false;
    }
    return true;
}
```

## 总结体会

本题要求判断第一个字符串ransom能否由第二个字符串magazine组成，即第二个字符串需要含有第一个字符串所有字母。

在算法设计上，采用的hash表，哈希表大小定义为256。建立2个哈希表hash1和hash2，分别统计每个字符串出现的次数，最后比较hash1和hash2，返回第二个字符串是否符合要求。

