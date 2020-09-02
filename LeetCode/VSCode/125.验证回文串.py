#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        lp, rp = 0, n-1
        while lp < rp:
            while lp < rp and not s[lp].isalnum():
                lp += 1
            while lp < rp and not s[rp].isalnum():
                rp -= 1
            if lp < rp:
                if s[lp].lower() != s[rp].lower():
                    return False
                lp, rp = lp + 1, rp - 1
        return True

# @lc code=end

