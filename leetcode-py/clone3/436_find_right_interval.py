#
# 436. Find Right Interval
#
# Q: https://leetcode.com/problems/find-right-interval/
# A: https://leetcode.com/problems/find-right-interval/discuss/814963/Javascript-Python3-C%2B%2B-Lower-Bound
#

from typing import List
from bisect import bisect_left

class Solution:
    def findRightInterval(self, A: List[List[int]]) -> List[int]:
        m = {}
        for k, [i, j] in enumerate(A):
            m[i] = k
        keys = sorted(m.keys())
        ans = []
        for [i, j] in A:
            k = bisect_left(keys, j)
            ans.append(m[keys[k]] if k < len(A) else -1)
        return ans
