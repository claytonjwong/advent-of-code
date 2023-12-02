#
# 152. Maximum Product Subarray
#
# Q: https://leetcode.com/problems/maximum-product-subarray/
# A: https://leetcode.com/problems/maximum-product-subarray/discuss/48233/Javascript-Python3-C%2B%2B-MinMax-solutions
#

from typing import List

class Solution:
    def maxProduct(self, A: List[int]) -> int:
        lo = A[0]
        hi = A[0]
        best = A[0]
        for i in range(1, len(A)):
            next = [A[i], lo * A[i], hi * A[i]]
            lo, hi = min(next), max(next)
            best = max(best, hi)
        return best
