#
# 289. Game of Life
#
# Q: https://leetcode.com/problems/game-of-life/
# A: https://leetcode.com/problems/game-of-life/discuss/607337/Kt-Js-Py3-Cpp-In-Place-LIVE-or-DIE
#

from typing import List

class Solution:
    def gameOfLife(self, A: List[List[int]]) -> None:
        M = len(A)
        N = len(A[0])
        for i in range(M):
            for j in range(N):
                k = 0
                for u, v in [[i - 1, j], [i - 1, j + 1], [i, j + 1], [i + 1, j + 1], [i + 1, j], [i + 1, j - 1], [i, j - 1], [i - 1, j - 1]]:
                    if 0 <= u < M and 0 <= v < N and 0 < A[u][v]:
                        k += 1
                if 0 < A[i][j]:
                    A[i][j] = k if k == 2 or k == 3 else 1      # 🙂 live cells must have 2 or 3 adjacent live cells to stay alive, otherwise k = 1 (special case)
                else:
                    A[i][j] = -k                                # 👻 dead cells have -k adjacent live cells
        for i in range(M):
            for j in range(N):
                if 0 < A[i][j]:
                    A[i][j] = int(A[i][j] == 2 or A[i][j] == 3)  # 🙂 live cells must have 2 or 3 adjacent live cells to stay alive
                else:
                    A[i][j] = int(A[i][j] == -3)                 # 👻 dead cells become alive with 3 adjacent live cells
