#
# 1446. Consecutive Characters
#
# Q: https://leetcode.com/problems/consecutive-characters/
# A: https://leetcode.com/problems/consecutive-characters/discuss/639815/Kt-Js-Py3-Cpp-Best-Same
#

# last
class Solution:
    def maxPower(self, s: str, last = '0', same = 1, best = 1) -> int:
        for c in s:
            if last == c:
                same += 1; best = max(best, same)
            else:
                last = c; same = 1
        return best

# index
class Solution:
    def maxPower(self, s: str, same = 1, best = 1) -> int:
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                same += 1; best = max(best, same)
            else:
                same = 1
        return best
