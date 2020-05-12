# Longest Common Prefix

## 问题分析
Write a function to find the longest common prefix string amongst an array of strings.

编写一个函数来查找字符串数组中最长的公共前缀字符串。

## 代码实现

1.
``` C
char* longestCommonPrefix(char** strs, int strsSize) {
	int n = strsSize;
	if (n == 0) return "";
	int sign = 0;
	int i = 0;
	int j = 0;
	for (j; j < strlen(*strs); j++) {
		for (int i = 1; i < n; i++) {
			if (strs[0][j] != strs[i][j] || j>strlen(strs[i])) {
				sign = 1;
				break;
			}
		}
	  if (sign!=0) break;
	}
	if (j == 0) return "";
	char* result = (char*)malloc (j + 1);
	for (i = 0; i < j; i++) {
		result[i] = strs[0][i];
	}
	  result[j] = '\0';
	return result;
}
```

2.
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = min(strs, key=len)
        for s in strs:
            for j in range(len(res)):
                if s[j] != res[j]:
                    res = res[:j]
                    break
        return res
```

## 总结体会

本题虽定级为Easy，但是做起来相当有难度。

首先需要理解题目所给函数中strsSize含义，指的是字符串数组中进行比较的是几组字符串，用于确定比较范围；

其次，理解二级指针的含义，二级指针保存的是一级指针的地址，它的类型是指针变量，
而一级指针保存的是指向数据所在的内存单元的地址，虽然都是地址，但是类型不同；

再次，选用较为简单的逐项比较法，即在0-strsSize之间的字符串，从第一位开始比较，直至有不同的位停止，之间的字符串即为共同前缀字符串；

最后将字符串return返回输出。

方法二：  
首先将字符串中最短的作为预先判断；对列表中每一个元素s，用res寻找最小公共前缀。