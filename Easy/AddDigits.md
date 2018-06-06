#  Add Digits

## 问题分析
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Follow up: Could you do it without any loop/recursion in O(1) runtime?

给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

进阶: 你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？

## 代码实现
``` C
int addDigits(int num) {
    int sum;
    if(num<10)  return num;  
    else{  
        sum=0;
        while(num!=0){
            sum+=num%10;
            num/=10;
        }  
        return addDigits(sum); 
    }  
}

int addDigits(int num) {
     if(num == 0) return 0;  
     if(num % 9 == 0) return 9;   
        else return num % 9;  
}
```

## 总结体会

本题主要考察一个非负整数经过循环计算，最终得到一个一位数的过程。

在算法设计上，第一种方法是递归法，当num小于10时，直接返回num值，当num大于或等于10时进行各位相加循环，直至结果为1位数。

由于题目进阶要求，所以采用观察法得到第二种方法，num值为9的倍数时，最终的个位数为9，其他情况下，个位数的值均为num % 9，得到第二个函数。满足不使用循环或者递归且在 O(1) 时间复杂度内解决的条件要求。