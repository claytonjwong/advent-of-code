#
# 1582. Special Positions in a Binary Matrix
#
# Q: https://leetcode.com/problems/special-positions-in-a-binary-matrix
# A: https://leetcode.com/problems/special-positions-in-a-binary-matrix/discuss/843916/Kt-Js-Py3-Cpp-Sum-Row-and-Column
#

from typing import List

class Solution:
    def numSpecial(self, A: List[List[int]], cnt = 0) -> int:
        M = len(A)
        N = len(A[0])
        row = [0] * M
        col = [0] * N
        for i in range(M):
            for j in range(N):
                if A[i][j]:
                    row[i] += 1
                    col[j] += 1
        for i in range(M):
            for j in range(N):
                if A[i][j] and row[i] == 1 and col[j] == 1:
                    cnt += 1
        return cnt
