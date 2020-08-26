#  Count Primes

## 问题分析

Count the number of prime numbers less than a non-negative number, n.

统计所有小于非负数整数 n 的质数的数量。


## 代码实现

1.
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

2.
```python
class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        label = [1] * (n)
        if n < 2:
            return 0
        for i in range(2, n):
            k = 2
            mul = k * i
            if label[i] == 1:
                count += 1
            while mul < n:
                label[mul] = 0
                k += 1
                mul = k * i
        return count
```

3.埃拉托斯特尼筛法
```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0
        for i in range(2,int(n ** 0.5)+1):
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * ((n-1-i*i)//i+1)
        return sum(isPrime)

```

## 总结体会

本题要求所有小于非负数整数 n 的质数个数。

在算法设计上采用埃拉托斯特尼筛法，首先把1删除（既不是质数也不是合数）；其次从2开始遍历到n的平方根，先找到第一个质数2，然后将其所有的倍数全部标记出来，isPrime[j]=0，再次是标记3的所有倍数；最后未被标记isPrime[i]=1的个数即为符合要求的质数的个数。

方法三：效率提升的关键在于埃拉托斯特尼筛法，简称埃式筛，也叫厄拉多塞筛法：要得到自然数n以内的全部质数，必须把不大于根号n的所有质数的倍数剔除，剩下的就是质数。  
isPrime = [1] * n，这一句初始化一个存放n个元素的列表 isPrime，元素初始值为1，表示该元素所在的位置索引值是一个质数，这样一来我们不用单独开辟内存用于存放数字，下标索引天生就可以用来表示自然数。  
if isPrime[i]: 判断第 i 个数是否已经被赋值为 0 ，即对之前已经排除掉的不是质数的数，不用再对它的倍数进行二次排除。注意：埃式筛要排除的是所有小于等于根号n的质数的倍数，而不是所有小于等于根号n的数的倍数。  
isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1) 指定步长参数，进行列表切片赋值，之所以从 i 的平方开始，是因为小于 i 的平方的倍数部分，在它之前就已经被排除掉了。return sum(isPrime) 到这里列表中每个质数位的值均为 1 ，其余合数位的值均为 0 ，sum(isPrime)的结果就是 n 以内质数的个数。

还是要看清楚埃氏筛这一句：要得到自然数n以内的全部质数，必须把不大于根号n的所有质数的倍数剔除，剩下的就是质数。