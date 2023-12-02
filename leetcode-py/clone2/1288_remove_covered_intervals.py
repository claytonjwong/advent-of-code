#
# 1288. Remove Covered Intervals
#
# Q: https://leetcode.com/problems/remove-covered-intervals/
# A: https://leetcode.com/problems/remove-covered-intervals/discuss/457523/Javascript-Python3-C%2B%2B-Sort-%2B-Linear-Scan
#

from typing import List

class Solution:
    def removeCoveredIntervals(self, A: List[List[int]], x = 0) -> int:
        A.sort(key = cmp_to_key(lambda a, b: b[1] - a[1] if a[0] == b[0] else a[0] - b[0]))
        ok = lambda a, b: a[0] <= b[0] and b[1] <= a[1]
        N = len(A)
        i = 0
        j = 1
        while j < N:
            if ok(A[i], A[j]):
                x += 1
                j += 1
            else:
                i = j
                j += 1
        return N - x
