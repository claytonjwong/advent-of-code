#
# 498. Diagonal Traverse
#
# Q: https://leetcode.com/problems/diagonal-traverse/
# A: https://leetcode.com/problems/diagonal-traverse/discuss/986121/Kt-Js-Py3-Cpp-Traverse-(Up-%2B-Right)
#

from typing import List

class Solution:
    def findDiagonalOrder(self, A: List[List[int]]) -> List[int]:
        rev = 0
        diags = []
        M = len(A)
        N = len(A[0]) if M else 0
        def diag(i, j):                    # traverse diag 👆 👉  (up + right)
            nonlocal rev
            res = []
            while 0 <= i and j < N:
                res.append(A[i][j])
                i -= 1
                j += 1
            if rev:
                res.reverse()
            rev ^= 1
            return res
        for i in range(M):                 # first column
            diags.extend(diag(i, 0))
        for j in range(1, N):              # last row
            diags.extend(diag(M - 1, j))
        return diags
