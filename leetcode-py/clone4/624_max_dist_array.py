#
# 624. Maximum Distance in Arrays
#
# Q: https://leetcode.com/problems/maximum-distance-in-arrays/
# A: https://leetcode.com/problems/maximum-distance-in-arrays/discuss/104653/Javascript-Python3-C%2B%2B-MinMax-solutions
#

from typing import List

class Solution:
    def maxDistance(self, A: List[List[int]], best = 0) -> int:
        N = len(A)
        lo = lambda i: A[i][0]
        hi = lambda i: A[i][len(A[i]) - 1]
        minimum, maximum = lo(0), hi(0)
        for i in range(1, N):
            best = max(best, abs(minimum - hi(i)), abs(maximum - lo(i)))
            minimum = min(minimum, lo(i))
            maximum = max(maximum, hi(i))
        return best
