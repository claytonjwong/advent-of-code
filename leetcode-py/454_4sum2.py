#
# 454. 4Sum II
#
# Q: https://leetcode.com/problems/4sum-ii/
# A: https://leetcode.com/problems/4sum-ii/discuss/975519/Kt-Js-Py3-Cpp-Map
#

from typing import List
from collections import Counter

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        m = Counter(a + b for a in A for b in B)
        return sum([m[-(c + d)] for c in C for d in D if -(c + d) in m])
