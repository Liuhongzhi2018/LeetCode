# Length of Last Word

## 问题分析
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string. If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。


## 代码实现
``` C
int lengthOfLastWord(char* s) {
	int n = strlen(s);
	if (n == 0) return 0;
	int count = 0;
	int i=n-1;
	int sign=0;
	while (i >= 0) {
		if (s[i] != ' ') {
			count++;
			sign = 1;
			i--;
		}
		if (s[i] == ' ') {
			i--;
			if (sign) break;
		}
	}
	return count;
}
```

## 总结体会
本题要求最后一个单词的长度，采用的不同以往从前向后的程序设计思想，而是从后向前查找的思路。从最后一位开始遍历字符串元素，遇到字母前的空格元素忽略，当开始有单词出现时标志位由0为1，计算字母个数；再遇到空格时，如果前面出现过单词，则循环终止，返回字母个数。
