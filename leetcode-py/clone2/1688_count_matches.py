#
# 1688. Count of Matches in Tournament
#
# Q: https://leetcode.com/problems/count-of-matches-in-tournament/
# A: https://leetcode.com/problems/count-of-matches-in-tournament/discuss/970250/Kt-Js-Py3-Cpp-1-Liners
#

class Solution:
    def numberOfMatches(self, N: int) -> int:
        return 0 if N == 1 else N // 2 + self.numberOfMatches(N // 2 + int(N & 1))
