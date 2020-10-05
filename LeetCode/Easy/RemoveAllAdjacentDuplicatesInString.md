# Remove All Adjacent Duplicates In String

## 问题描述

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。


## 代码实现

1.同向双指针
```python
class Solution:
    def removeDuplicates(self, S: str) -> str:
        if S == '' or len(S) < 2:  return S
        slist = list(S)
        lp = 0
        rp = lp + 1
        while lp < len(slist) and rp < len(slist):
            if slist[lp] != slist[rp]:
                lp += 1
                rp += 1
            else:
                slist.pop(rp)
                slist.pop(lp)
                lp -= 1
                lp = 0 if lp < 0 else lp
                rp = lp + 1
        return ''.join(slist)
```

2.单调栈
```python
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for s in S:
            if stack and s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)
        return "".join(stack)
```

## 思考总结

方法一：同向双指针  
首先将字符串转换为列表，lp和rp分别代表前后指针，如果两个元素相同则抛出相同的两个元素，直到前指针指向位置0的元素，否则前后指针同时向后移位。

方法二：单调栈