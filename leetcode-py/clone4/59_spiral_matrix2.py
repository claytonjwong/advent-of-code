#
# 59. Spiral Matrix II
#
# Q: https://leetcode.com/problems/spiral-matrix-ii/
# A: https://leetcode.com/problems/spiral-matrix-ii/discuss/430457/Kt-Js-Py3-Cpp-Step-and-Turn-Right
#

from typing import List

class Solution:
    def generateMatrix(self, N: int) -> List[List[int]]:
        A = [[0] * N for _ in range(N)]
        i = 0
        j = 0
        k = 0
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # clockwise 👆, 👉, 👇, 👈
        steps = 1
        A[i][j] = steps; steps += 1
        while steps <= N * N:
            while True:
                u = i + dirs[k][0]
                v = j + dirs[k][1]
                if 0 <= u < N and 0 <= v < N and not A[u][v]:
                    i, j = u, v
                    A[i][j] = steps; steps += 1
                else:
                    break
            k = (k + 1) % 4
        return A
