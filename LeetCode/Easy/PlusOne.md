# Plus One  

## 问题分析
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。


## 代码实现
``` C
int* plusOne(int* digits, int digitsSize, int* returnSize){
	int i;
	int add = 1;
	int temp = 0;
	int* returns;
	for (i = digitsSize - 1; i >= 0; i--)
	{
		temp = (digits[i] + add) % 10;
		add = (digits[i] + add) / 10;
		digits[i] = temp;
	}
	if (add == 1)
	{
		returns = (int *)malloc(sizeof(int)*(digitsSize + 1));
		returns[0] = 1;
		for (i = 0; i<digitsSize; i++)
			returns[i + 1] = digits[i];
		*returnSize = digitsSize + 1;
		return returns;
	}
	if (add == 0)
	{
		*returnSize = digitsSize;
		return digits;
	}
}
```

## 总结体会
本题要求将所给数组代表的数值加1后返回，主要考察两种情况，一种是不进位则元素个数不变，另一种是各位均为9时进位，则动态分配空间，在原数组长度基础上加1。
