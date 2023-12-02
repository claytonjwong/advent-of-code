#
# 456. 132 Pattern
#
# Q: https://leetcode.com/problems/132-pattern/
# A: https://leetcode.com/problems/132-pattern/discuss/907505/Kt-Js-Py3-Cpp-Trivial-solutions
#

from typing import List

class Solution:
    def find132pattern(self, A: List[int]) -> bool:
        N = len(A)
        first = A[0]
        for j in range(1, N):
            first = min(first, A[j])  # ⭐️ minimum A[i] seen so far
            for k in range(j + 1, N):
                if first < A[k] < A[j]:
                    return True
        return False
