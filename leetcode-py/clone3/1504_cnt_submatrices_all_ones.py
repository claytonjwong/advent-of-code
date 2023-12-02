#
# 1504. Count Submatrices With All Ones
#
# Q: https://leetcode.com/problems/count-submatrices-with-all-ones/
# A: https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/762330/Kt-Js-Py3-Cpp-Brute-Force
#

from typing import List

class Solution:
    def numSubmat(self, A: List[List[int]], total = 0) -> int:
        def go(row, col, cnt = 0):
            M = len(A)
            N = len(A[0])
            for i in range(row, M):
                for j in range(col, N):
                    if A[i][j]:
                        cnt += 1
                    else:
                        N = j
                        break
            return cnt
        M = len(A)
        N = len(A[0])
        for i in range(M):
            for j in range(N):
                total += go(i, j) # 🎯 count of all submatrices starting with i,j as top-left corner
        return total
