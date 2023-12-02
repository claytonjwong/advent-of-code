#
# 1608. Special Array With X Elements Greater Than or Equal X
#
# Q: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
# A: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/discuss/877706/Javascript-Python3-C%2B%2B-Lower-Bound-(ie.-Binary-Search)
#

from typing import List
from bisect import bisect_left

class Solution:
    def specialArray(self, A: List[int]) -> int:
        N = len(A)
        A.sort()
        for i in range(N + 1):
            if bisect_left(A, i) == N - i:
                return i
        return -1
