#
# 1463. Cherry Pickup II
#
# Q: https://leetcode.com/problems/cherry-pickup-ii/
# A: https://leetcode.com/problems/cherry-pickup-ii/discuss/660828/Kt-Js-Py3-Cpp-The-ART-of-Dynamic-Programming
#

from typing import List

# top-down
class Solution:
    def cherryPickup(self, A: List[List[int]]) -> int:
        M = len(A)
        N = len(A[0])
        def go(k = 0, i = 0, j = N - 1):
            if k == M:
                return 0
            best = 0
            for u in [i - 1, i, i + 1]:
                for v in [j - 1, j, j + 1]:
                    if not (u < 0 or v < 0 or u == M or v == N or v <= u):
                        best = max(best, go(k + 1, u, v))
            return A[k][i] + A[k][j] + best
        return go()

# top-down w/ memo
class Solution:
    def cherryPickup(self, A: List[List[int]]) -> int:
        M = len(A)
        N = len(A[0])
        @cache
        def go(k = 0, i = 0, j = N - 1):
            if k == M:
                return 0
            best = 0
            for u in [i - 1, i, i + 1]:
                for v in [j - 1, j, j + 1]:
                    if not (u < 0 or v < 0 or u == M or v == N or v <= u):
                        best = max(best, go(k + 1, u, v))
            return A[k][i] + A[k][j] + best
        return go()

# bottom-up
class Solution:
    def cherryPickup(self, A: List[List[int]]) -> int:
        M = len(A)
        N = len(A[0])
        dp = [[[0] * N for _ in range(N)] for _ in range(M + 1)]
        for k in range(M - 1, -1, -1):
            for i in range(N):
                for j in range(N):
                    for u in [i - 1, i, i + 1]:
                        for v in [j - 1, j, j + 1]:
                            if not (u < 0 or v < 0 or u == M or v == N or v <= u):
                                dp[k][i][j] = max(dp[k][i][j], A[k][i] + A[k][j] + dp[k + 1][u][v])
        return dp[0][0][N - 1]

# bottom-up mem-opt
class Solution:
    def cherryPickup(self, A: List[List[int]]) -> int:
        M = len(A)
        N = len(A[0])
        pre = [[0] * N for _ in range(N)]
        for k in range(M - 1, -1, -1):
            cur = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for u in [i - 1, i, i + 1]:
                        for v in [j - 1, j, j + 1]:
                            if not (u < 0 or v < 0 or u == M or v == N or v <= u):
                                cur[i][j] = max(cur[i][j], A[k][i] + A[k][j] + pre[u][v])
            pre, cur = cur, pre
        return pre[0][N - 1]
