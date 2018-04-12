# Valid Parentheses

## 问题分析
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

括号必须以正确的顺序关闭，"()" 和 "()[]{}" 是有效的但是 "(]" 和 "([)]" 不是。

## 代码实现
``` C
bool isValid(char* s) {  
    char a[1000000];  
    int i=-1;  
    while(*s!='\0'){  
        if(*s==')'){  
            if(i>=0 && a[i]=='(')i--;  
            else return false;  
        }
        if(*s=='}'){  
            if(i>=0 && a[i]=='{')i--;  
            else return false;  
        }if(*s==']'){  
            if(i>=0 && a[i]=='[')i--;  
            else return false;  
        }
        else a[++i]=*s;   
        s++;  
    }  
    return i==-1;  
}  
```

## 总结体会
本题采用出栈的思想，当遇到左半符号时，若栈内有右半符号，即符合要求。
