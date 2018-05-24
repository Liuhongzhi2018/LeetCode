#  Count Primes

## 问题分析
Count the number of prime numbers less than a non-negative number, n.

统计所有小于非负数整数 n 的质数的数量。


## 代码实现
``` C
int countPrimes(int n) {
    int i,j;
    int count=0;
    if(n<=2)  return 0;
    bool *isPrime = (bool *)malloc(sizeof(bool)*n);
    memset(isPrime, 1, sizeof(bool)*n);
   for (i = 2; i * i< n; i++) {
      if (!isPrime[i])  continue;
      for (j = i * i; j < n; j += i)    isPrime[j] = 0;
   }
   for (i = 2; i < n; i++) 
      if (isPrime[i])   count++;
   return count;
}
```

## 总结体会

本题要求所有小于非负数整数 n 的质数个数。

在算法设计上采用埃拉托斯特尼筛法，首先把1删除（既不是质数也不是合数）；其次从2开始遍历到n的平方根，先找到第一个质数2，然后将其所有的倍数全部标记出来，isPrime[j]=0，再次是标记3的所有倍数；最后未被标记isPrime[i]=1的个数即为符合要求的质数的个数。