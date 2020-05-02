#  Reverse Bits

## 问题分析
Reverse bits of a given 32 bits unsigned integer.

Follow up: If this function is called many times, how would you optimize it?

颠倒给定的 32 位无符号整数的二进制位。

进阶: 如果多次调用这个函数，你将如何优化你的算法？


## 代码实现
``` C
uint32_t reverseBits(uint32_t n) {
        uint32_t bits = 0;
        for (int i = 0; i < 32; ++i) {
            if (n & 1 == 1) {
                bits = (bits << 1) + 1;
            } else {
                bits = bits << 1;
            }
            n = n >> 1;
        }
        return bits;
    }
```

## 总结体会

本题要求颠倒无符号二进制整数，采用的算法是将待翻转的数n从右向左进行和1的与运算按位取出，然后重新排列。

首先给定一个32位全零数bits，如果待翻转数n右边第一位的是1，我们将结果bits左移一位并且加上1；如果待翻转数n右边第一位是0，我们将bits左移一位。完成一次移位操作，n右移一位，最后二进制数bits返回。