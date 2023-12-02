#
# 1007. Minimum Domino Rotations For Equal Row
#
# Q: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
# A: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/discuss/252219/Kt-Js-Py3-Cpp-Brute-Force
#

from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        def rotate(cur, alt, T, cnt = 0):
            for i in range(N):
                if cur[i] == T:
                    continue
                if alt[i] == T:
                    cnt += 1
                else:
                    return float('inf')
            return cnt
        cand = [ rotate(A, B, A[0]), rotate(A, B, B[0]),
                 rotate(B, A, A[0]), rotate(B, A, B[0]) ]
        return -1 if all([ cnt == float('inf') for cnt in cand ]) else min(*cand)
