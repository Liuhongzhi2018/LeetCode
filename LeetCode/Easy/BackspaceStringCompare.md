#  Backspace String Compare

## 问题分析

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。


## 代码实现

1.单调栈
```python
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        charS = [] 
        charT = [] 
        for i in S: 
            if i != '#': 
                charS.append(i) 
            else: 
                if charS: 
                    charS.pop() 
        for j in T: 
            if j != '#': 
                    charT.append(j) 
            else: 
                if charT: 
                    charT.pop() 
        return ''.join(charS) == ''.join(charT) 
```
2.双指针
```python
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def F(S): 
            skip = 0 
            for x in reversed(S): 
                if x == '#': 
                    skip += 1 
                elif skip: 
                    skip -= 1 
                else: 
                    yield x 
        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))
```


## 总结体会

双指针算法：  
一个字符是否属于最终字符串的一部分，取决于它后面有多少个退格符。  
如果反向遍历字符串，就可以先知道有多少个退格符，然后知道退格符左边有多少个字符会被删除，对应的也就知道哪些字符会保留在最终的字符串中。

算法  
反向遍历字符串，如果遍历到一个退格符，那么再往左第一个非退格字符将会被删除，剩余未被删除的字符就是最终的字符串。