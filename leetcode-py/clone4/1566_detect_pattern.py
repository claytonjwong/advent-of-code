#
# 1566. Detect Pattern of Length M Repeated K or More Times
#
# Q: https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
# A: https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/discuss/819276/Javascript-Python3-C%2B%2B-T-Pieces-Whole
#

from typing import List

class Solution:
    def containsPattern(self, A: List[int], K: int, T: int) -> bool:
        j = K * T
        for i in range(0, len(A) - j + 1):
            piece = A[i:i + K]
            whole = T * piece
            if whole == A[i:i + j]:
                return True
        return False
