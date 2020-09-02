#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for e in t:
            need[e] += 1
        length = len(t)
        ret = (0,float('inf'))
        lp = 0
        for rp, v in enumerate(s):
            if need[v] > 0:
                length -= 1
            need[v] -= 1
            if length == 0:
                while True:
                    cur = s[lp]
                    if need[cur] == 0:
                        break
                    need[cur] += 1
                    lp += 1
                if rp - lp < ret[1]-ret[0]:
                    ret = (lp,rp)
                need[s[lp]] += 1
                length += 1
                lp += 1
        return '' if ret[1]>len(s) else s[ret[0]:ret[1]+1]


# @lc code=end

