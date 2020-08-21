#  Restore IP Addresses

## 问题描述

Given a string s containing only digits. Return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single points and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。

## 代码实现

1.深度优先搜索DFS
``` python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        NUM = 4
        
        def DFS(start, path):
            if len(path) > NUM or  (len(path)==NUM and start < len(s)-1):
                return 
            if start >= len(s):
                if len(path) == NUM:
                    ans.append('.'.join(path))
                return
            
            if s[start] == '0':
                path.append(s[start])
                DFS(start+1, path)
                path.pop()
                return

            for i in range(start, len(s)):
                if 0 <= int(s[start:i+1]) <= 255:
                    path.append(s[start:i+1])
                    DFS(i+1, path)
                    path.pop()
                else:
                    break
            return
        
        ans = []
        DFS(0, [])
        return ans
```

2.递归法
```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        SEG_COUNT = 4 
        ans = list() 
        segments = [0] * SEG_COUNT 
        
        def dfs(segId: int, segStart: int): 
            # 如果找到了 4 段 IP 地址并且遍历完了字符串，那么就是一种答案 
            if segId == SEG_COUNT: 
                if segStart == len(s): 
                    ipAddr = ".".join(str(seg) for seg in segments) 
                    ans.append(ipAddr) 
                return 
                
            # 如果还没有找到 4 段 IP 地址就已经遍历完了字符串，那么提前回溯 
            if segStart == len(s): 
                return 
                
            # 由于不能有前导零，如果当前数字为 0，那么这一段 IP 地址只能为 0 
            if s[segStart] == "0": 
                segments[segId] = 0 
                dfs(segId + 1, segStart + 1) 
                
            # 一般情况，枚举每一种可能性并递归 
            addr = 0 
            for segEnd in range(segStart, len(s)): 
                addr = addr * 10 + (ord(s[segEnd]) - ord("0")) 
                if 0 < addr <= 0xFF: 
                    segments[segId] = addr 
                    dfs(segId + 1, segEnd + 1) 
                else: 
                    break 
            
        dfs(0, 0) 
        return ans
```


## 思路总结

DFS法。定义DFS函数，查找在[0,255]之间的数字，然后再查找下一层。

递归法。由于我们需要找出所有可能复原出的 IP 地址，因此可以考虑使用递归的方法，对所有可能的字符串分隔方式进行搜索，并筛选出满足要求的作为答案。设题目中给出的字符串为 s。我们用递归函数 dfs(segId,segStart)表示我们正在从 s[segStart]的位置开始，搜索 IP 地址中的第 segId 段，其中 segId∈{0,1,2,3}。由于 IP 地址的每一段必须是 [0,255]中的整数，因此我们从 segStart 开始，从小到大依次枚举当前这一段 IP 地址的结束位置 segEnd。如果满足要求，就递归地进行下一段搜索，调用递归函数 dfs(segId+1,segEnd+1)。  
特别地，由于 IP 地址的每一段不能有前导零，因此如果 s[segStart]等于字符 0，那么 IP 地址的第 segId 段只能为 000，需要作为特殊情况进行考虑。  
在递归搜索的过程中，如果我们已经得到了全部的 4 段 IP 地址（即 segId=4），并且遍历完了整个字符串（即 segStart=∣s∣，其中 ∣s∣ 表示字符串 s 的长度），那么就复原出了一种满足题目要求的 IP 地址，我们将其加入答案。在其它的时刻，如果提前遍历完了整个字符串，那么我们需要结束搜索，回溯到上一步。