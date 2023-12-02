#
# 1673. Find the Most Competitive Subsequence
#
# Q: https://leetcode.com/problems/find-the-most-competitive-subsequence/
# A: https://leetcode.com/problems/find-the-most-competitive-subsequence/discuss/952775/Kt-Js-Py3-Cpp-Monotonic-Queue
#

from typing import List

class Solution:
    def mostCompetitive(self, A: List[int], K: int) -> List[int]:
        S = []
        N = len(A)
        i = 0
        while i < N:
            if len(S) and A[i] < S[-1] and i + K - len(S) < N:  # 📈 maintain monotonic queue invariant
                S.pop()
            else:
                S.append(A[i])
                i += 1
        return S[:K]
