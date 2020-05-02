#  Binary Watch

## 问题分析
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

Note:

* The order of output does not matter.
* The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
* The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。

注意事项:

* 输出的顺序没有要求。
* 小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
* 分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。

## 代码实现
``` C
/**
* Return an array of size *returnSize.
* Note: The returned array must be malloced, assume caller calls free().
*/
int oneNum(int i)
{
    int n = 0;
    while (i){
        if (i % 2 == 1)   n++;
        i /= 2;
    }
    return n;
}
char** readBinaryWatch(int num, int* returnSize) {
    int hour, min, len = 0;
    char buf[6] = { 0 };
    char** result = (char**)malloc(12 * 60 * sizeof(char*));
    if (num > 10 || num < 0) return result;
    for (hour = 0; hour<12; hour++){
        for (min = 0; min<60; min++){
            if (oneNum(hour * 64 + min) == num){
                result[len] = (char*)malloc(6 * sizeof(char));
                sprintf(buf, "%d", hour);
                strcat(result[len], buf);
                strcat(result[len], ":");
            if (min / 10 == 0)   strcat(result[len], "0");
                sprintf(buf, "%d", min);
                strcat(result[len], buf);
                len++;
            }
        }
    }
    *returnSize = len;
    return result;
}
```

## 总结体会

本题要求根据给定的手表显示点数，罗列出所有可能的时间，实际上可以理解为求符合要求点数的所有二进制数。

在算法设计上，首先需要查找出符合点数要求的二进制数，采用嵌套for循环和oneNum函数进行判断，直到高4位小时与低6位分钟的点数等于num；其次初始化字符串buf，使用sprintf将hour变量保存在buf中，用strcat进行字符串连接；而且需要注意小时和分钟的要求，最后返回result即为所求时间。



