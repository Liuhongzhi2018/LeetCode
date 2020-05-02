#  Implement Stack Using Queues

## 问题分析
Implement the following operations of a stack using queues.

* push(x) -- Push element x onto stack.
* pop() -- Removes the element on top of the stack.
* top() -- Get the top element.
* empty() -- Return whether the stack is empty.

使用队列实现栈的下列操作：

* push(x) -- 元素 x 入栈
* pop() -- 移除栈顶元素
* top() -- 获取栈顶元素
* empty() -- 返回栈是否为空

## 代码实现
``` C
typedef struct {
    int* var;
    int size;
    int top;
} MyStack;

/** Initialize your data structure here. */
MyStack* myStackCreate(int maxSize) {
    MyStack* str;
    str = (struct MyStack*)malloc(sizeof(MyStack));
    str->var = (int*)malloc(sizeof(int)*maxSize);
    str->top = -1;
    str->size = maxSize;
    return str;
}

/** Push element x onto stack. */
void myStackPush(MyStack* obj, int x) {
    if (obj->top + 1<obj->size)
    {
        obj->top++;
        *(obj->var + obj->top) = x;
    }
}

/** Removes the element on top of the stack and returns that element. */
int myStackPop(MyStack* obj) {
    if (obj->top - 1>-2)
    {
        int x = *(obj->var + obj->top);
        obj->top--;
        return x;
    }
    return 0;
}

/** Get the top element. */
int myStackTop(MyStack* obj) {
    return *(obj->var + obj->top);
}

/** Returns whether the stack is empty. */
bool myStackEmpty(MyStack* obj) {
    if (obj->top == -1)
        return true;
    return false;
}

void myStackFree(MyStack* obj) {
    free(obj->var);
}

/**
* Your MyStack struct will be instantiated and called as such:
* struct MyStack* obj = myStackCreate(maxSize);
* myStackPush(obj, x);
* int param_2 = myStackPop(obj);
* int param_3 = myStackTop(obj);
* bool param_4 = myStackEmpty(obj);
* myStackFree(obj);
*/
```

## 总结体会

本题要求用队列实现栈的操作，需要理解队列的数据结构，并进行栈的基本操作。

在算法设计上，首先定义一个结构体类型MyStack，包含三个成员即int型指针变量var，size是长度，top是栈顶变量。其次分别用函数实现创建栈数据结构、入栈、出栈、栈顶位置、判断是否空栈以及释放内存空间的操作，完成栈的基本操作，实现数据结构的变换。