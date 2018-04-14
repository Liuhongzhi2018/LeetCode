
# Roman to Integer

## 问题描述
Given a roman numeral,　convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.

给定一个罗马数字，将其转换成整数。返回的结果要求在 1 到 3999 的范围内。

## 代码实现
``` C
int romanToInt(char* s) {
	int n = 0;
	int a[10];
	int value = 0;
	while (s[n]!='\0'){
		switch (s[n]){
		case 'I': a[n] = 1; break;
		case 'V': a[n] = 5; break;
		case 'X': a[n] = 10; break;
		case 'L': a[n] = 50; break;
		case 'C': a[n] = 100; break;
		case 'D': a[n] = 500; break;
		case 'M': a[n] = 1000; break;
		default:  break;
		}
		n++;
	}
	for (int i = 0; i < n; i++) {
		if (a[i] < a[i + 1])
			value -= a[i];
		else value += a[i];
	}
	return value;
}
```
## 总结体会
此编程题，我首先了解了罗马数字的组成方式，不仅是常用的I、V、X而且还有其他的字母表示，以及代表数值；
其次，熟悉了switch-case语句的使用；
最后实现本题的要求目标。
