# Remove Element

## 问题分析
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

## 代码实现
``` C
int removeElement(int* nums, int numsSize, int val) {
	int i = 0;
	int j = 0;
	if (numsSize == 0)  return 0;
	while (j<numsSize){
		if (nums[j] == val) {
			j++;
		}
		else{
			nums[i] = nums[j++];
			printf("%d, ",nums[i]);
			i++;
		}
	}
	return i;
}
```

## 总结体会

经过上一题删除排序数组中的重复项的训练，本题难度就有所降低，所用算法类似。

本题方法是，数组中元素依次与待比较数值value进行对比判断，如果相等则指向下一个元素进行比较，不同的元素保存到新数组中，同样采用两个变量i和j指向不同元素。
