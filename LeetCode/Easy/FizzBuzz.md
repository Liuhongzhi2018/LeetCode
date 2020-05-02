#  Fizz Buzz

## 问题分析
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

写一个程序，输出从 1 到 n 数字的字符串表示。如果 n 是3的倍数，输出“Fizz”；如果 n 是5的倍数，输出“Buzz”；如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

## 代码实现
``` C
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** fizzBuzz(int n, int* returnSize) {
    *returnSize = n;
    char buf[11]={0};
    char** ret = (char**)malloc(sizeof(char*)*n);
    int i;
    for (i = 0; i<n;i++){
        ret[i] =(char *) malloc(sizeof(buf));
        if ((i+1) % 15 ==0)  sprintf(buf, "%s", "FizzBuzz");
        else if ((i+1) % 3 == 0)  sprintf(buf, "%s", "Fizz");
        else if ((i+1) % 5 == 0)  sprintf(buf, "%s", "Buzz");
        else sprintf(buf, "%d", i+1);
        memcpy(ret[i], buf, strlen(buf) + 1);
    }
    return ret;
}

```

## 总结体会

本题要求将所给的从1开始到指定范围的自然数中，将对应3、5和15倍数的数字，分别用Fizz、Buzz和FizzBuzz字符串表示，需要注意的是因为15是3和5的最小公倍数，应该优先判断是否为15倍数。

在算法设计上，首先声明一个二维字符串ret，用以保存转换的字符串；其次用for循环对数字进行遍历，因为数列从1开始，判断时i应该+1，用sprintf函数将对应倍数的字符串按照\%s字符串格式保存到buf缓冲区；最后用memcpy函数将buf内容拷贝到ret字符串中，返回ret字符串即为所求。


