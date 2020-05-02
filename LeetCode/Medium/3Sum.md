#  3Sum

## 问题分析
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

## 代码实现
``` C
/**
 * Return an array of arrays of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int** threeSum(int* nums, int numsSize, int* returnSize); 
int cmp(const void *a,const void *b);

int** threeSum(int* nums, int numsSize, int* returnSize) {
    int row=0,begin,end,dif,l;
    if(nums == NULL||numsSize < 3)  return NULL;
    int com = (numsSize)*(numsSize-1)*(numsSize-2)/6;
    int **ret=(int **)malloc(sizeof(int *)*com);
    qsort(nums,numsSize,sizeof(nums[0]),cmp); 
    for(int i=0;i<numsSize;i++){
        begin=i+1;
        end=numsSize-1;
        while(begin<end){
            dif=nums[i]+nums[begin]+nums[end];
            if(dif==0){
                     ret[row]=(int *)malloc(3*sizeof(int));
                    if(ret[row]==NULL)  exit(EXIT_FAILURE);
                    ret[row][0]=nums[i];
                    ret[row][1]=nums[begin];
                    ret[row][2]=nums[end];
                    for(l=0;l<row;l++) {
                        if(ret[l][0]==ret[row][0]&&ret[l][1]==ret[row][1]&&ret[l][2]==ret[row][2]){
                            free(ret[row]);
                            ret[row]=NULL;
                            row--;
                        }
                    }
                    row++; 
                    begin++;
            } 
            else if(dif<0)  begin++;
            else   end--;
        }
    }           
    *returnSize=row;
    return ret;
}
int cmp(const void *a,const void *b){
    return (*((int *)a))-*((int *)b);
}

```

## 总结体会

本题要求从含n个整数的数组中，找出满足和为零的三元素组合，实际上需要将找出组合数并且满足加和为零的条件。

在算法设计上，首先声明一个用于返回元素组合的二维数组，套用组合数公式得到大小；其次将数组进行排序,，直接调用qsort函数进行快排；若满足和为零的题目要求，就将该三数组元素依次保存在数组中，并检查若出现重复和释放内存空间；最后将得到的数组返回。

