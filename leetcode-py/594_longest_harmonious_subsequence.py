#
# 594. Longest Harmonious Subsequence
#
# Q: https://leetcode.com/problems/longest-harmonious-subsequence/
# A: https://leetcode.com/problems/longest-harmonious-subsequence/discuss/846353/Javascript-Python3-C%2B%2B-Map-solutions
#

from typing import List
import collections

class Solution:
    def findLHS(self, A: List[int], best = 0) -> int:
        m = collections.Counter(A)
        for x, _ in m.items():
            if x - 1 in m:
                best = max(best, m[x - 1] + m[x])
        return best
