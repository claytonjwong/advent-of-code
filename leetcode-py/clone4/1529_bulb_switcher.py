#
# 1529. Bulb Switcher IV
#
# Q: https://leetcode.com/problems/bulb-switcher-iv/
# A: https://leetcode.com/problems/bulb-switcher-iv/discuss/755780/Javascript-Python3-C%2B%2B-count-bit-flips
#
class Solution:
    def minFlips(self, s: str, cur = '0', cnt = 0) -> int:
        for c in s:
            if cur != c:
                cur = c
                cnt += 1
        return cnt
