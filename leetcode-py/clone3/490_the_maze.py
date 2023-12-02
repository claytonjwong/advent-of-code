#
# 490. The Maze
#
# Q: https://leetcode.com/problems/the-maze/
# A: https://leetcode.com/problems/the-maze/discuss/806498/Javascript-Python3-C%2B%2B-DFS-solutions
#

from typing import List

class Solution:
    def hasPath(self, A: List[List[int]], start: List[int], target: List[int]) -> bool:
        seen = set()
        M = len(A)
        N = len(A[0]) if M else 0
        def go(i, j):
            if i == target[0] and j == target[1]:  # 🎯 target
                return True
            for row, col in [[-1, 0], [0, 1], [1, 0], [0, -1]]:  # [👆, 👉, 👇, 👈 ]
                u, v = i, j
                # 1. 🚌 continue in same direction until 💥 collision
                while 0 <= u < M and 0 <= v < N and not A[u][v]:
                    u += row
                    v += col
                # 2. 🚀 recursively explore previous position proceeding 💥 collision
                u -= row
                v -= col
                if f'{u},{v}' in seen:
                    continue
                seen.add(f'{u},{v}')
                if go(u, v):
                    return True
            return False
        return go(start[0], start[1])
