#
# 849. Maximize Distance to Closest Person
#
# Q: https://leetcode.com/problems/maximize-distance-to-closest-person/
# A: https://leetcode.com/problems/maximize-distance-to-closest-person/discuss/137957/Kt-Js-Py3-Cpp-Distance-from-LeftRight
#

from typing import List

class Solution:
    def maxDistToClosest(self, A: List[int]) -> int:
        best = 0
        N = len(A)
        L = [N] * N
        R = [N] * N
        if A[0]:
            L[0] = 0
        if A[N - 1]:
            R[N - 1] = 0
        for i in range(1, N):
            L[i] = 0 if A[i] else 1 + L[i - 1]  # distance from (L)eft-to-right 👉
        for i in range(N - 2, -1, -1):
            R[i] = 0 if A[i] else 1 + R[i + 1]  # distance from (R)ight-to-left 👈
        for i in range(N):
            best = max(best, min(L[i], R[i]))
        return best
