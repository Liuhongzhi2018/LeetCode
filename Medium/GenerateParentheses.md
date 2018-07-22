# Generate Parentheses

## 问题分析
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. 

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。


## 代码实现
``` C
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
void generate(char** comb,int* size,int l,int r,char* tmp,int index){
    if(!l && !r){
        tmp[index]=0;
        comb[*size]=(char*)malloc(sizeof(char)*index);
        strcpy(comb[*size],tmp);
        (*size)++;
        return;
    }
    if(l){
        tmp[index]='(';
        generate(comb,size,l-1,r,tmp,index+1);
    }
    if(r && l<r){
        tmp[index]=')';
        generate(comb,size,l,r-1,tmp,index+1);
    }s
}
char** generateParenthesis(int n, int* returnSize) {
    char** comb;
    char* tmp=(char*)malloc(sizeof(char)*(2*n+1));
    int l,r;
    l=r=n;
    comb=(char**)malloc(sizeof(char*)*1000000);
    *returnSize=0;
    generate(comb,returnSize,l,r,tmp,0);
    return comb;
}
```

## 总结体会
本题要求括号的组合，根据返回函数可知是用二位数组保存所有的组合。

在算法设计上，首先二维数组comb用于保存括号组合，l和r分别代表左右括号的个数；其次采用递归的算法，在generate函数中排列出括号的所有组合情况，每产生一次左右括号，变量l和r递减1；最后组合的括号保存在二维数组中返回。