#  Nim Game

## 问题分析
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

你和你的朋友，两个人一起玩 Nim游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。你作为先手。

你们是聪明人，每一步都是最优解。 编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。

## 代码实现
``` C
bool canWinNim(int n) {
    return n % 4;
}
```

## 总结体会

本题要求判断在给定石头数量情况下能否在当前游戏规则下胜利。通过题目的提示，如果给定数量为4将无法赢得比赛，返回false。通过归纳推理，只要给定为4的倍数，同样没有办法胜利，返回false。只有当给定为非4的倍数时，返回true。

