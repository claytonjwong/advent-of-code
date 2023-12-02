#
# 1368. Minimum Cost to Make at Least One Valid Path in a Grid
#
# Q: https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
# A: https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/discuss/529142/Kt-Js-Py3-Cpp-BFS
#

from typing import List
from collections import deque

class Solution:
    def minCost(self, A: List[List[int]]) -> int:
        M = len(A)
        N = len(A[0])
        best = [[float('inf')] * N for _ in range(M)]
        best[0][0] = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque([[0, 0, 0]])
        seen = set()
        while q:
            i, j, cost = q.popleft()
            for dir, (di, dj) in enumerate(dirs):
                u = i + di
                v = j + dj
                w = cost + (1 if A[i][j] != dir + 1 else 0)
                key = f'{u},{v},{w}'
                if 0 <= u < M and 0 <= v < N and key not in seen and w < best[u][v]:
                    q.append([u, v, w])
                    seen.add(key)
                    best[u][v] = w
        return best[M - 1][N - 1]
