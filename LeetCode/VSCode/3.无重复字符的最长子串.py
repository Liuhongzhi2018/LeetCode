#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        point2 = 0 
        result = [] 
        ans = 0 
        for i in range(len(s)): 
            if i > 0: 
                result.remove(s[i - 1]) 
            while point2 < len(s) and s[point2] not in result: 
                result.append(s[point2]) 
                point2 += 1 
            ans = max(ans, point2 - i) 
        return ans

# @lc code=end