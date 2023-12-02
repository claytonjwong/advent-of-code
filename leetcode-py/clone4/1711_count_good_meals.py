#
# 1711. Count Good Meals
#
# Q: https://leetcode.com/problems/count-good-meals/
# A: https://leetcode.com/problems/count-good-meals/discuss/1001864/Kt-Js-Py3-Cpp-Map-%2B-Brute-Force-Search
#

from typing import List

class Solution:
    def countPairs(self, A: List[int], cnt = 0) -> int:
        m = {}
        for x in A:
            t = 1
            while t <= 1 << 21:
                y = t - x
                if y in m:
                    cnt = (cnt + m[y]) % int(1e9 + 7)
                t <<= 1
            m[x] = 1 + m[x] if x in m else 1
        return cnt
