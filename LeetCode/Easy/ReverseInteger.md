
# Reverse Integer

## 问题分析

Given a 32-bit signed integer, reverse digits of an integer.

给定一个范围为 32 位 int 的整数，将其颠倒。
注意:
假设我们的环境只能处理 32 位 int 范围内的整数。根据这个假设，如果颠倒后的结果超过这个范围，则返回 0。

## 编程实现
1.
``` C
int reverse(int x) {
    int i;
    int n = 0;
    if (x < 0) {
	printf("-");
        i = 0 - x;
	}
	do {
           printf("%d", i % 10);
           n++;
           if (n>32) break;
	} while ((i /= 10) != 0);

     if (n <= 32) return i;
     else return 0;
}
```

2.
```python
class Solution:
    def reverse(self, x: int) -> int:
        strx = str(x)
        x = int('-'+strx[1:][::-1]) if x < 0 else int(strx[::-1])
        return 0 if x<-2**31 or x > 2**31-1 else x
```

3.纯数学方式
```python
class Solution:
    def reverse(self, x: int) -> int:
        flag = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x:
            res = res*10+x%10
            x //=10
        res *= flag
        return 0 if res<-2**31 or res>2**31-1 else res
```

## 总结体会

整数颠倒输出时，需要考虑各个数位上值的变化。除从个位向高位输出的方法外，还可以考虑使用字符数组输出。

首先判断是否为正数，如果是就直接翻转，如果不是则取出符号后进行翻转；  
最后判断是否在取值范围内，是就返回，否则返回0。