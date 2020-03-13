# 剑指Offer

## 学习文档

[数据结构](https://www.bilibili.com/video/av86803650?from=search&seid=1397237482083708915)

[剑指offer-数据结构与算法](https://www.bilibili.com/video/av64288683/?spm_id_from=333.788.videocard.2)


## 题目清单


### 数组 (Array) (11道)：

数组是最简单的一种数据结构，它占据一块连续的内存并按照顺序存储数据。创建数组时需要首先指定数组的容量大小，然后根据大小分配内存，即使只在数组中存储一个数组，也需要为所有的数据预先分配内存，因此空间效率不高，但是时间效率高。

根据时间效率高的优点可用数组实现简单的哈希表，数组下标设为哈希表的键值Key，数组的元素设为哈希表的值Value，组成一个键值-值配对。

解决数组空间效率不高的问题可设计动态数组。先开辟小空间添加数据，当数目超过数组容量时重新分配更大空间，之前数据复制到新数组，释放之前的内存。

在C/C++中数组和指针相互关联又区别，当声明数组时，数组名也是一个指针，指针指向数组的第一个元素，访问元素时，要确保没有超出数组的边界。

* [剑指Offer（一）：二维数组中的查找](http://cuijiahua.com/blog/2017/11/basis_1.html)
* [剑指Offer（六）：旋转数组的最小数字](http://cuijiahua.com/blog/2017/11/basis_6.html)
* [剑指Offer（十三）：调整数组顺序使奇数位于偶数前面](http://cuijiahua.com/blog/2017/11/basis_13.html)
* [剑指Offer（二十八）：数组中出现次数超过一半的数字](http://cuijiahua.com/blog/2017/12/basis_28.html)
* [剑指Offer（三十）：连续子数组的最大和](http://cuijiahua.com/blog/2017/12/basis_30.html)
* [剑指Offer（三十二）：把数组排成最小的数](http://cuijiahua.com/blog/2018/01/basis_32.html)
* [剑指Offer（三十五）：数组中的逆序对](http://cuijiahua.com/blog/2018/01/basis_35.html)
* [剑指Offer（三十七）：数字在排序数组中出现的次数](http://cuijiahua.com/blog/2018/01/basis_37.html)
* [剑指Offer（四十）：数组中只出现一次的数字](http://cuijiahua.com/blog/2018/01/basis_40.html)
* [剑指Offer（五十）：数组中重复的数字](http://cuijiahua.com/blog/2018/01/basis_50.html)
* [剑指Offer（五十一）：构建乘积数组](http://cuijiahua.com/blog/2018/01/basis_51.html)


|                  Title                   |                  Python                  |                   C++                    |                   Blog                   |
| :--------------------------------------: | :--------------------------------------: | :--------------------------------------: | :--------------------------------------: |
|     二维数组中的查找                   | [Python](https://github.com/Liuhongzhi2018/LeetCode/blob/master/SwordOffer/Array_1.md) | |
|     数组中重复的数字                   | [Python](https://github.com/Liuhongzhi2018/LeetCode/blob/master/SwordOffer/Array_2.md) | |
|     构建乘积数组                   | [Python](https://github.com/Liuhongzhi2018/LeetCode/blob/master/SwordOffer/Array_3.md) | |

### 字符串 (String) (8道):

字符串是由若干字符组成的序列。

* [剑指Offer(二)：替换空格](http://cuijiahua.com/blog/2017/11/basis_2.html "悬停显示")
* [剑指Offer（二十七）：字符串的排列](http://cuijiahua.com/blog/2017/12/basis_27.html "悬停显示")
* [剑指Offer（三十四）：第一个只出现一次的字符](http://cuijiahua.com/blog/2018/01/basis_34.html "悬停显示")
* [剑指Offer（四十三）：左旋转字符串](http://cuijiahua.com/blog/2018/01/basis_43.html "悬停显示")
* [剑指Offer（四十四）：翻转单词顺序序列](http://cuijiahua.com/blog/2018/01/basis_44.html "悬停显示")
* [剑指Offer（四十九）：把字符串转换成整数](http://cuijiahua.com/blog/2018/01/basis_49.html "悬停显示")
* [剑指Offer（五十二）：正则表达式匹配](http://cuijiahua.com/blog/2018/01/basis_52.html "悬停显示")
* [剑指Offer（五十三）：表示数值的字符串](http://cuijiahua.com/blog/2018/01/basis_53.html "悬停显示")

|                  Title                   |                  Python                  |                   C++                    |                   Blog                   |
| :--------------------------------------: | :--------------------------------------: | :--------------------------------------: | :--------------------------------------: |
|     替换空格                   | [Python](https://github.com/Liuhongzhi2018/LeetCode/blob/master/SwordOffer/String_1.md) | |
|     正则表达式匹配                   | [Python](https://github.com/Liuhongzhi2018/LeetCode/blob/master/SwordOffer/String_2.md) | |
|     表示数值的字符串                   | [Python](https://github.com/Liuhongzhi2018/LeetCode/blob/master/SwordOffer/String_3.md) | |
|     字符流中第一个不重复的字符                   | [Python](https://github.com/Liuhongzhi2018/LeetCode/blob/master/SwordOffer/String_4.md) | |

### 链表 (LinkedList) (8道)


* [剑指Offer（三）：从尾到头打印链表](http://cuijiahua.com/blog/2017/11/basis_3.html "悬停显示")
* [剑指Offer（十四）：链表中倒数第k个结点](http://cuijiahua.com/blog/2017/12/basis_14.html "悬停显示")
* [剑指Offer（十五）：反转链表](http://cuijiahua.com/blog/2017/12/basis_15.html "悬停显示")
* [剑指Offer（十六）：合并两个排序的链表](http://cuijiahua.com/blog/2017/12/basis_16.html "悬停显示")
* [剑指Offer（二十五）：复杂链表的复制](http://cuijiahua.com/blog/2017/12/basis_25.html "悬停显示")
* [剑指Offer（三十六）：两个链表的第一个公共结点](http://cuijiahua.com/blog/2018/01/basis_36.html "悬停显示")
* [剑指Offer（五十五）：链表中环的入口结点](http://cuijiahua.com/blog/2018/01/basis_55.html "悬停显示")
* [剑指Offer（五十六）：删除链表中重复的结点](http://cuijiahua.com/blog/2018/01/basis_56.html "悬停显示")

|                  Title                   |                  Python                  |                   C++                    |                   Blog                   |
| :--------------------------------------: | :--------------------------------------: | :--------------------------------------: | :--------------------------------------: |
|      从尾到头打印链表                    | [Python](https://github.com/Liuhongzhi2018/LeetCode/blob/master/SwordOffer/LinkedList_1.md) | |
|      链表中环的入口结点                    | [Python](https://github.com/Liuhongzhi2018/LeetCode/blob/master/SwordOffer/LinkedList_2.md) | |