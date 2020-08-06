#  Reverse Vowels of a String

## 问题分析
Write a function that takes a string as input and reverse only the vowels of a string.

Note: The vowels does not include the letter "y".

编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

注意: 元音字母不包括 "y".

## 代码实现
1.
``` C
void swap(char *a, char *b);
bool isVowel(char c);
char* reverseVowels(char* s);

void swap(char *a, char *b){
    char temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
bool isVowel(char c){
    c = tolower(c);
    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')   return true;
    else  return false;
}
char* reverseVowels(char* s) {
    int len = strlen(s);
    if (len == 0)  return s;
    int i, j;
    for (i = 0, j = len - 1; i < j;) {
        if (isVowel(s[i]) && isVowel(s[j]))      swap(s+i, s+j), i++, j--;
        if (isVowel(s[i]) && !isVowel(s[j]))     j--;
        if (!isVowel(s[i]) && isVowel(s[j]))     i++;
        if (!isVowel(s[i]) && !isVowel(s[j]))    i++, j--;
    }
    return s;
}
```

2. 双指针法
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 1 or len(s) == 0:
            return s
        lp, rp = 0, len(s) - 1
        yuanlist = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        sl = list(s)
        while lp <= rp:
            if sl[lp] in yuanlist and sl[rp] in yuanlist:
                sl[lp], sl[rp] = sl[rp], sl[lp]
                rp -= 1
                lp += 1
            elif sl[lp] in yuanlist and sl[rp] not in yuanlist:
                rp -= 1
            elif sl[lp] not in yuanlist and sl[rp] in yuanlist:
                lp += 1
            else:
                rp -= 1
                lp += 1
        return ''.join(sl)

```

## 总结体会

本题主要考察字符串的操作，即字符串的遍历和字符互换等。

在算法设计上，首先判断是否为空字符串；然后用两个指针从首尾向中间来遍历字符串元素；其次用isVowel(char c)函数判断是否有符合要求的元音字母a，e，i，o，u（不包括y），若是返回true；再次，如果此时所指均为元音字母，用void swap(char *a, char *b)函数互换字母；最后返回遍历完成并交换元音之后的字符串s。

首先将需要交换位置的大小写元音字母保存到列表中便于快速判断是否是元音字符，并且将给定字符串转换为列表；然后使用双指针，一个从头遍历，一个从尾遍历，当同时遍历到元音字符时交换元素；当其中一个指针找到元音字母时，移动另一个指针，一次遍历便可以完成交换，循环终止条件是两个指针重合。

