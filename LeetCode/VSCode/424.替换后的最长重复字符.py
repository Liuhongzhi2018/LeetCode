#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slen = len(s)
        if k > slen:
            return slen
        s_dict = collections.defaultdict(int)
        max_val, ret = 0, 0
        lp = 0
        for rp in range(slen):
            s_dict[s[rp]] += 1
            max_val = max(max_val, s_dict[s[rp]])
            while rp - lp + 1 - max_val > k:
                s_dict[s[lp]] -= 1
                lp += 1
            ret = max(ret, rp - lp + 1)
        return ret
        

# @lc code=end

