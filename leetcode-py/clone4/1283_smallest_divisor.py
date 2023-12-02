#
# 1283. Find the Smallest Divisor Given a Threshold
#
# Q: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
# A: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/discuss/925931/Kt-Js-Py3-Cpp-Binary-Search
#

from math import ceil
from typing import List

class Solution:
    def smallestDivisor(self, A: List[int], T: int) -> int:
        f = lambda div: sum([ ceil(num / div) for num in A ])
        i = 1
        j = int(1e6)
        while i < j:
            k = (i + j) // 2
            if T < f(k):
                i = k + 1
            else:
                j = k
        return i
