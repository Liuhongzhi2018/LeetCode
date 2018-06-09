#  First Bad Version

## 问题分析
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

## 代码实现
``` C
// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

int firstBadVersion(int n) {
    int front = 1, rear = n, mid;
    while (front != rear) {
        //mid = ((long)front + rear) / 2;
        mid = front + (rear - front) / 2;
        if (isBadVersion(mid) == true)  rear = mid;
        else front = mid + 1;
    }
    return front;
}
```

## 总结体会

本题要求找出错误版本，可以转换为二分查找第一个符合错误版本的序号。

首先应该了解，错误版本信息是由isBadVersion的API接口返回，调用API可以知道当前版本是否有错误。其次因为要求尽可能少的调用API，在算法判断时采用二分查找法找第一个错误。将mid值传递给API函数，如果是错误版本，说明第一个错误在左边，则把mid赋值给rear，如果是正确版本，则说明第一个错误在右边，则把mid+1赋给front，最后返回front值所代表的版本返回。

值得注意的是，直接编写 mid = (left + right) / 2 会超出时间限制，采用两种方式改正，一是mid = front + (rear - front) / 2；二是 mid = ((long)front + rear) / 2，OJ通过Accepted。