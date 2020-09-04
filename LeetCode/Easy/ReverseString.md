#  Reverse String

## 问题分析

Write a function that takes a string as input and returns the string reversed.

给定一个整数 (32位有符整数型)，请写出一个函数来检验它是否是4的幂。

请编写一个函数，其功能是将输入的字符串反转过来。

## 代码实现

1.
``` C
char* reverseString(char* s) {
    int i;
    char temp;
    int len = strlen(s);
    if (len == 0)   return s;
    for (i = 0; i < len / 2; i++) {
        temp = s[i];
        s[i] = s[len-1 - i];
        s[len-1 - i] = temp;
    }
    return s;
}
```

2.双指针法
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lp, rp = 0, len(s)-1
        while lp < rp:
            s[lp], s[rp] = s[rp], s[lp]
            lp += 1
            rp -= 1
```

## 总结体会

本题主要考察字符串的操作。

在算法设计上，首先求出字符串长度，然后将字符串首尾对应元素依次互换，采用的是for循环和临时变量交换元素的方法，最后返回重新排序的字符串。

双指针法是使用两个指针，一个左指针 left，右指针 right，开始工作时 left 指向首元素，right 指向尾元素。交换两个指针指向的元素，并向中间移动，直到两个指针相遇。  
算法实现上将lp指向首元素，rp指向尾元素，当lp < rp时交换s[lp] 和s[rp]，然后lp和rp分别向右和左移动一步。