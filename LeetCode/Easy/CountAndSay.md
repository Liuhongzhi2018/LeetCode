# Count and Say

## 问题描述

The count-and-say sequence is the sequence of integers.

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

报数序列是指一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。

1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n ，输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

## 代码实现
``` C
char* countAndSay(int n) {
	if (n <= 0) return "";
	if (n == 1) return "1";
	char * a = (char *)malloc(2);
	char * temp;
	a[0] = '1';
	a[1] = '\0';
	int len, cur, j, count;
	for (int i = 2; i <= n; i++) {
		len = strlen(a);
		temp = (char *)malloc(3 * len);
		memset(temp, 0, 3 * len);
		count = 1;
		for (cur = 1, j = 0; cur < len; cur++) {
			if (a[cur] == a[cur - 1]) count++;
			else {
				temp[j++] = '0' + count;
				temp[j++] = a[cur - 1];
				count = 1;
			}
		}
		temp[j++] = '0' + count;
		temp[j] = a[len - 1];
		free(a);
		a = temp;
	}
	return a;
}
```

## 总结体会

本题主要考察规律的算法实现，第n行的字符串元素主要取决于第n-1行的字符串组成。

在编程实现时，主要困难在于数组长度的初始化定义，尝试使用动态内存分配的方法对临时数组的长度进行初始化，然后将前一行字符串连续相同元素个数作为第n行的元素，进而组成第n个字符串。