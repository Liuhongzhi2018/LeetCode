#
# @lc app=leetcode.cn id=457 lang=python3
#
# [457] 环形数组循环
#

# @lc code=start
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for lp in range(n):
            s = set()
            pos = lp
            posLast = pos
            flag = 0
            while pos not in s:
                flag = 1
                s.add(pos)
                posLast = pos
                pos = (pos + nums[pos] + n) % n
                if nums[pos] * nums[lp] < 0:
                    flag = 2
                    break
            if pos == posLast:
                continue
            if len(s) > 1 and flag == 1:
                return True
        return False
        
# @lc code=end

