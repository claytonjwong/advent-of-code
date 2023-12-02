#
# 980. Unique Paths III
#
# Q: https://leetcode.com/problems/unique-paths-iii/
# A: https://leetcode.com/problems/unique-paths-iii/discuss/856143/Kt-Js-Py3-Cpp-DFS-%2B-BT
#

from typing import List

class Solution:
    def uniquePathsIII(self, A: List[List[int]], total = 0, paths = 0) -> int:
        M = len(A)
        N = len(A[0])
        for i in range(M):
            for j in range(N):
                if A[i][j] == 0: total += 1
                if A[i][j] == 1: s = [i, j]
                if A[i][j] == 2: t = [i, j]
        def go(i, j, steps = -1):
            nonlocal paths
            if t[0] == i and t[1] == j:
                if steps == total:
                    paths += 1
                return
            for u, v in [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]]:
                if 0 <= u < M and 0 <= v < N and (not A[u][v] or A[u][v] == 2):
                    A[u][v] = -1
                    go(u, v, steps + 1)
                    A[u][v] = 0
            return paths
        return go(s[0], s[1])
