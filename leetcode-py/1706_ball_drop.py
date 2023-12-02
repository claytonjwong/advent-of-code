#
# 1706. Where Will the Ball Fall
#
# Q: https://leetcode.com/problems/where-will-the-ball-fall/
# A: https://leetcode.com/problems/where-will-the-ball-fall/discuss/988174/kt-js-py3-cpp-simulation-recursive-iterative
#

from typing import List

# Recursive Concise
class Solution:
    def findBall(self, A: List[List[int]]) -> List[int]:
        ans = []
        M = len(A)
        N = len(A[0])
        drop = lambda i, j: j if i == M else drop(i + 1, j + A[i][j]) if 0 <= j < N and 0 <= j + A[i][j] < N and A[i][j] == A[i][j + A[i][j]] else -1
        return [drop(0, j) for j in range(N)]

# Recursive Verbose
class Solution:
    def findBall(self, A: List[List[int]]) -> List[int]:
        ans = []
        M = len(A)
        N = len(A[0])
        def drop(i, j):
            if i == M:
                return j
            return drop(i + 1, j + A[i][j]) if 0 <= j < N and 0 <= j + A[i][j] < N and A[i][j] == A[i][j + A[i][j]] else -1
        return [drop(0, j) for j in range(N)]

# Iterative
class Solution:
    def findBall(self, A: List[List[int]]) -> List[int]:
        ans = []
        M = len(A)
        N = len(A[0])
        for k in range(N):
            i = 0
            j = k
            while i < M and 0 <= j < N and 0 <= j + A[i][j] < N and A[i][j] == A[i][j + A[i][j]]:
                j += A[i][j]; i += 1
            ans.append(j if i == M else -1)
        return ans
