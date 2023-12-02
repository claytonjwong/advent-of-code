#
# 704. Binary Search
#
# Q: https://leetcode.com/problems/binary-search/discuss/
# A: https://leetcode.com/problems/binary-search/discuss/600517/Javascript-Python3-C%2B%2B-Lower-Bound
#

from typing import List
from bisect import bisect_left

class Solution:
    def search(self, A: List[int], T: int) -> int:
        N = len(A)
        i = bisect_left(A, T)
        return i if i != N and A[i] == T else -1
