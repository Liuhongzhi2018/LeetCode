#!/usr/bin/env python
# coding=utf-8

def fib_fun(n):
    result = [0,1]
    for i in range(n-2):
        result.append(result[-2] + result[-1])
    return result

if __name__ == "__main__":
    lst = fib_fun(10)
    print(lst)
