#
# 593. Valid Square
#
# Q: https://leetcode.com/problems/valid-square/
# A: https://leetcode.com/problems/valid-square/discuss/932012/Kt-Js-Py3-Cpp-Map
#

from collections import Counter
from typing import List

class Solution:
    def validSquare(self, a: List[int], b: List[int], c: List[int], d: List[int]) -> bool:
        m = Counter()
        f = lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2)
        A = [ a, b, c, d ]
        for i in range(4):
            for j in range(i + 1, 4):
                m[f(*A[i], *A[j])] += 1
        return len(m) <= 2 and all(0 < x and (cnt == 2 or cnt == 4 or cnt == 6) for x, cnt in m.items())
