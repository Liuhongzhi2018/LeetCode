#  Reverse Vowels of a String

## 问题分析
Write a function that takes a string as input and reverse only the vowels of a string.

Note: The vowels does not include the letter "y".

编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

注意: 元音字母不包括 "y".

## 代码实现
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

## 总结体会

本题主要考察字符串的操作，即字符串的遍历和字符互换等。

在算法设计上，首先判断是否为空字符串；然后用两个指针从首尾向中间来遍历字符串元素；其次用isVowel(char c)函数判断是否有符合要求的元音字母a，e，i，o，u（不包括y），若是返回true；再次，如果此时所指均为元音字母，用void swap(char *a, char *b)函数互换字母；最后返回遍历完成并交换元音之后的字符串s。

