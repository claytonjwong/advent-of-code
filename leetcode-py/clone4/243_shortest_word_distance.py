#
# 243. Shortest Word Distance
#
# Q: https://leetcode.com/problems/shortest-word-distance/
# A: https://leetcode.com/problems/shortest-word-distance/discuss/670999/Kt-Js-Py3-Cpp-Last-Seen-K-th-Index
#

from typing import List

class Solution:
    def shortestDistance(self, A: List[str], s: str, t: str, i = -1, j = -1, best = 1e9 + 7) -> int:
        for k, word in enumerate(A):
            if word == s: i = k
            if word == t: j = k
            if -1 < i and -1 < j:
                best = min(best, abs(i - j))
        return best
