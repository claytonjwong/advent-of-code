#
# 994. Rotting Oranges
#
# Q: https://leetcode.com/problems/rotting-oranges/
# A: https://leetcode.com/problems/rotting-oranges/discuss/782008/Javascript-Python3-C%2B%2B-BFS-solutions
#

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, A: List[List[int]], depth = 0, need = 0) -> int:
        q, seen = deque(), set()
        M = len(A)
        N = len(A[0])
        for i in range(M):
            for j in range(N):
                if A[i][j] == 1:
                    need += 1
                elif A[i][j] == 2:
                    q.append([ i, j ])
                    seen.add(f'{i},{j}')
        if not need:
            return 0
        while q:
            k = len(q)
            while k:
                i, j = q.popleft()
                for u, v in [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]]:
                    if not (u < 0 or u == M or v < 0 or v == N or f'{u},{v}' in seen) and A[u][v] == 1:
                        need -= 1
                        q.append([ u, v ])
                        seen.add(f'{u},{v}')
                k -= 1
            depth += 1
        return depth - 1 if not need else -1

Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])