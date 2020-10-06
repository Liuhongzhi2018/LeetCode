#  Longest Repeating Substring

## 问题描述

给定字符串 S，找出最长重复子串的长度。如果不存在重复子串就返回 0。


## 代码实现

1.二分查找
```C
class Solution {
public:
    int longestRepeatingSubstring(string S) {
    	int l = 0, r = S.size()-1, len, maxlen;
    	while(l <= r)
    	{
    		len = l+((r-l)>>1);
    		if(haveRepeat(S, len))
    			maxlen = len, l = len+1;
    		else
    			r = len-1;
    	}
    	return maxlen;
    }
    bool haveRepeat(string& S, int len)
    {
    	unordered_set<string> set;
    	string sub;
    	for(int i = 0; i <= S.size()-len; i++)
    	{
    		sub = S.substr(i, len);
    		if(!set.count(sub))
    			set.insert(sub);
    		else
    			return true;//有重复的子串
    	}
    	return false;
    }
};
```

2.动态规划
```C
class Solution(object):
    def longestRepeatingSubstring(self, S):
        """
        :type S: str
        :rtype: int
        """
        #动态规划， 用dp{（i, j）: length}表示 S[i - length + 1:i + 1] == S[j - length + 1: j + 1]
        ans = 0
        dp = {}
        for i in range(len(S)):
            for j in range(i + 1, len(S)):
                if S[i] == S[j]:
                    dp[(i,j)]=dp.get((i-1,j-1),0)+1
                    # print i, j, dp[(i, j)]
                    ans=max(ans,dp[(i,j)])
        return ans
```


## 思路总结

动态规划  
两重循环，如果当前位匹配上了，就把前一位DP记录下来的结果 + 1 赋给当前位DP。