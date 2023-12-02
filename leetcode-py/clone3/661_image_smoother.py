#
# 661. Image Smoother
#
# Q: https://leetcode.com/problems/image-smoother/
# A: https://leetcode.com/problems/image-smoother/discuss/599157/Javascript-and-C%2B%2B-solutions
#

from typing import List

class Solution:
    def imageSmoother(self, A: List[List[int]]) -> List[List[int]]:
        M = len(A)
        N = len(A[0])
        def scale(i, j):
            sum = A[i][j]
            cnt = 1
            for u, v in [[i - 1, j], [i - 1, j + 1], [i, j + 1], [i + 1, j + 1], [i + 1, j], [i + 1, j - 1], [i, j - 1], [i - 1, j - 1]]:
                if 0 <= u < M and 0 <= v < N:
                    sum += A[u][v]; cnt += 1
            return sum // cnt
        return [[scale(i, j) for j in range(N)] for i in range(M)]
