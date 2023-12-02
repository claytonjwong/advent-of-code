#
# 1620. Coordinate With Maximum Network Quality
#
# Q: https://leetcode.com/problems/coordinate-with-maximum-network-quality/
# A: https://leetcode.com/problems/coordinate-with-maximum-network-quality/discuss/898691/Kt-Js-Py3-Cpp-Brute-Force
#

from typing import List
from math import floor, sqrt
from functools import cmp_to_key

class Solution:
    def bestCoordinate(self, A: List[List[int]], radius: int) -> List[int]:
        N = len(A)
        quality = [0] * N
        A.sort(key = cmp_to_key(lambda a, b: a[1] - b[1] if a[0] == b[0] else a[0] - b[0]))  # lexicographical order
        dist = lambda x1, x2, y1, y2: sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)            # euclidean distance
        for i in range(N):
            x1, y1, q1 = A[i]
            quality[i] = q1
            for j in range(N):
                if i == j:
                    continue
                x2, y2, q2 = A[j]
                d = dist(x1, x2, y1, y2)
                if radius < d:
                    continue
                quality[i] += floor(q2 / (1 + d))
        best = max(quality)
        i = quality.index(best)
        return A[i][:2]
