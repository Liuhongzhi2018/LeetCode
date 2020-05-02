#  Min Stack

## 问题分析
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

* push(x) -- Push element x onto stack.
* pop() -- Removes the element on top of the stack.
* top() -- Get the top element.
* getMin() -- Retrieve the minimum element in the stack.

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

* push(x) -- 将元素 x 推入栈中。
* pop() -- 删除栈顶的元素。
* top() -- 获取栈顶元素。
* getMin() -- 检索栈中的最小元素。

## 代码实现
``` C
/**
 * Your MinStack struct will be instantiated and called as such:
 * struct MinStack* obj = minStackCreate(maxSize);
 * minStackPush(obj, x);
 * minStackPop(obj);
 * int param_3 = minStackTop(obj);
 * int param_4 = minStackGetMin(obj);
 * minStackFree(obj);
 */
typedef struct {  
    int* number;  
    int top;  
    int max;  
} MinStack;  
/** initialize your data structure here. */  
MinStack* minStackCreate(int maxSize) {  
    MinStack* obj;  
    obj=(MinStack*)malloc(sizeof(MinStack));  
    obj->number=(int*)malloc(sizeof(int)*maxSize);  
    obj->top=-1;  
    obj->max=maxSize;  
    return obj;  
}  
void minStackPush(MinStack* obj, int x) {  
    obj->top+=1;  
    *(obj->number+obj->top)=x;  
}  
void minStackPop(MinStack* obj) {  
    obj->top-=1;  
}  
int minStackTop(MinStack* obj) {  
    return *(obj->number+obj->top);  
} 
int minStackGetMin(MinStack* obj) {  
    int min=INT_MAX;  
    for(int n=0;n<=obj->top;n++) {  
        if(*(obj->number+n)<min)   min=*(obj->number+n);     
    }  
    return min;  
}  
void minStackFree(MinStack* obj) {  
    free(obj->number);  
    free(obj);  
}  
```

## 总结体会

本题要求设计能检索最小元素的栈，主要涉及到顺序栈的基本操作，包括初始化、入栈、出栈、读栈顶元素和释放空间等。

首先，定义MinStack的结构体类型，根据maxSize参数进行栈的初始化，在这里需要注意，必须有MinStack* obj;和obj=(MinStack*)malloc(sizeof(MinStack));语句，否则会出现 member access within null pointer of type 'struct' 的错误，因为无法判断obj栈是否为空，因而报错。其次，入栈push，top指针+1；出栈Pop，top指针-1；在GetMin函数中检索最小元素。最后释放malloc函数给指针变量分配的内存空间。











