#
# 74. Search a 2D Matrix
#
# Q: https://leetcode.com/problems/search-a-2d-matrix/
# A: https://leetcode.com/problems/search-a-2d-matrix/discuss/605294/Kt-Js-Py3-Cpp-Upper-Bound-(ie.-Binary-Search)
#

from typing import List
from bisect import bisect_right

class Solution:
    def searchMatrix(self, A: List[List[int]], T: int) -> bool:
        if not len(A) or not len(A[0]):
            return False
        first = [row[0] for row in A]
        row = bisect_right(first, T) - 1
        col = bisect_right(A[row], T) - 1
        return A[row][col] == T
