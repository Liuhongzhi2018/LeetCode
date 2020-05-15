# Valid Parentheses

## 问题分析
Given a string containing just the characters '(', ')',　'{', '}',　'[' and ']',　determine if the input string is valid.

The brackets must close in the correct order,　"()" and "()[]{}" are all valid but "(]" and "([)]" are not.

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

括号必须以正确的顺序关闭，"()" 和 "()[]{}" 是有效的但是 "(]" 和 "([)]" 不是。

## 代码实现
1.
``` C
bool isValid(char* s) {
	char a[1000000];
	int i = -1;
	while (*s!='\0') {
		if (*s == ')') {
			if (i >= 0 && a[i] == '(')i--;
			else return false;
		}
		else if (*s == '}') {
			if (i >= 0 && a[i] == '{')i--;
			else return false;
		}
		else if (*s == ']') {
			if (i >= 0 && a[i] == '[')i--;
			else return false;
		}
		else a[++i] = *s;
		s++;
	}
	return i == -1;
}
```

2.
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cache = {
            '(':')','[':']','{':'}'
        }
        for c in s:
            if c in cache:
                stack.append(c)
                continue
            if len(stack)==0 or cache[stack.pop()]!=c:
                return False
        return len(stack)==0

```

## 总结体会

本题采用出栈的思想，当遇到左半符号时，若栈内有右半符号，即符合要求。

用一个stack缓存所有见过的左括号，如果发现是右括号时，pop上面的括号看是否match，如果访问到最后一个元素并且stack为空，则返回True。用cache代表左括号map到右括号的字典，遍历所有s中的所有字符。

如果最后stack有剩余，则返回False。