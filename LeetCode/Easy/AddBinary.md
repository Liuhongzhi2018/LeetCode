# Add Binary  

## 问题描述

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。


## 代码实现

1.
``` C
char *addBinary(char *a, char *b) {
	int i;
	int len1 = strlen(a);
	int len2 = strlen(b);
	int len = len1>len2 ? len1 : len2;
	int Ci = 0;
	char *str;
	str = (char *)malloc(len + 2);
	memset(str, 0, len + 2);
	for (i = len; ; i--) {
		str[i] = (a[len1 - 1] - '0' + b[len2 - 1] - '0' + Ci) % 2 + '0';
		Ci = (a[len1 - 1] - '0' + b[len2 - 1] - '0' + Ci) / 2;
		len1--; len2--;
        if (len1 == 0 || len2 == 0)  { i--; break; }
	}
	if (len1 == 0) {
		for (; len2 > 0; i--) {
			str[i] = (b[len2 - 1] - '0' + Ci) % 2 + '0';
			Ci = (b[len2 - 1] - '0' + Ci) / 2;
			len2--;
		}
	}
	else if (len2 == 0) {
		for (; len1 >0; i--) {
			str[i] = (a[len1 - 1] - '0' + Ci) % 2 + '0';
			Ci = (a[len1 - 1] - '0' + Ci) / 2;
			len1--;
		}
	}
	if (Ci == 1) {
		str[i] = Ci + '0';
		return str + i;
	}
	return str + i + 1;
}
```

## 思考总结

本题所求为二进制无符号位的有进位加法，难点在于动态内存分配和最高位有进位时的字符串保存。与所学数字电路中一样，二进制加法从最低位开始加起，当最高位有进位时字符串数组长度会加1，然后将字符串返回输出，即可得到加法结果。
