#
# 1679. Max Number of K-Sum Pairs
#
# Q: https://leetcode.com/problems/max-number-of-k-sum-pairs/
# A: https://leetcode.com/problems/max-number-of-k-sum-pairs/discuss/962118/Kt-Js-Py3-Cpp-Map
#

from typing import List

class Solution:
    def maxOperations(self, A: List[int], T: int, cnt = 0) -> int:
        m = {}
        for x in A:
            y = T - x
            if y in m and m[y]:
                m[y] = -1 + (m[y] if y in m else 0); cnt += 1
            else:
                m[x] =  1 + (m[x] if x in m else 0)
        return cnt
