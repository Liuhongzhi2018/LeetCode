#  Guess Number Higher or Lower

## 问题分析
We are playing the Guess Game. The game is as follows: I pick a number from 1 to n. You have to guess which number I picked. Every time you guess wrong, I'll tell you whether the number is higher or lower. You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0).

我们正在玩一个猜数字游戏。 游戏规则如下：我从 1 到 n 选择一个数字。你需要猜我选择了哪个数字。每次你猜错了，我会告诉你这个数字是大了还是小了。你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）。

## 代码实现
``` C
// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int left = 1;
        int right = n;
        int mid,ans;
        while (left <= right) {
            mid = left + (right - left) / 2;
            ans = guess(mid);
            if (ans == 0)
                return mid;
            else if (ans < 0)
                right = mid - 1;
            else
                left = mid + 1;
        }
        return -1;
    }
};
```

## 总结体会

本题的猜数字游戏，可以转换为查找在一个数字范围区间的某一数字。

在算法设计上，采用二分查找法，首先将初值left和right分别赋值为范围的最小和最大值；其次在while循环中进行判断，直到返回answer变量为0，否则根据返回的ans改变查找范围。当返回ans为-1，范围最大值赋为中间值，当返回ans为1时，最小值为中间值。

