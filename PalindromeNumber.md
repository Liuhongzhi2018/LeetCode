# Palindrome Number

## 问题分析
Determine whether an integer is a palindrome. Do this without extra space.
判断一个整数是否是回文数。不能使用辅助空间。
一些提示:
负整数可以是回文数吗？（例如 -1）
如果你打算把整数转为字符串，请注意不允许使用辅助空间的限制。
你也可以考虑将数字颠倒。但是如果你已经解决了 “颠倒整数” 问题的话，就会注意到颠倒整数时可能会发生溢出。你怎么来解决这个问题呢？
本题有一种比较通用的解决方式。

## 代码实现
``` C
bool isPalindrome(int x) {
	int num = x;
	int ten = 1;
	if (num < 0)
		return false;
	do{
		ten *= 10;
	} while (num / ten <= 9);

	while (num != 0){
		int front = num / ten;
		int end = num % 10;
		if (front != end)
			return 0;
		num = (num % ten) / 10;
		ten /= 100;
	}
	return true;
}
```

## 总结体会
回文数要求正反读一样，转换为判断一个首尾数字相同，逐渐向中间逼近的思想。
