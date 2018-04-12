# Valid Parentheses

## 问题分析
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

括号必须以正确的顺序关闭，"()" 和 "()[]{}" 是有效的但是 "(]" 和 "([)]" 不是。

## 代码实现
``` C
bool isValid(char* s) {
	char *a = s;
	int n = strlen(a);
	int flag = 1;
	for (int i = 0; i < n; i++) {
		if (a[i] == '('&&a[i + 1] != ')') {
			flag = 0; break;
		}
		if (a[i] == '['&&a[i + 1] != ']') {
			flag = 0; break;
		}
		if (a[i] == '{'&&a[i + 1] != '}') {
			flag = 0; break;
		}
	}
	if (flag)  return true;
	else return false;
}
```

## 总结体会
本题比较简单，主要用到字符串内的操作。
我的方法是采用相邻元素比较，只要不满足配对，即为不符合要求。
