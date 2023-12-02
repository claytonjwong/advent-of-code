#
# 1572. Matrix Diagonal Sum
#
# Q: https://leetcode.com/problems/matrix-diagonal-sum/
# A: https://leetcode.com/problems/matrix-diagonal-sum/discuss/830407/Javascript-Python3-C%2B%2B-solutions
#

# 1-liner
class Solution:
    def diagonalSum(self, A: List[List[int]]) -> int:
        N = len(A)
        return sum([A[i][i] + A[i][N - 1 - i] for i in range(N)]) - (A[N // 2][N // 2] if N & 1 else 0)
# verbose
class Solution:
    def diagonalSum(self, A: List[List[int]], sum = 0) -> int:
        N = len(A)
        for i in range(N):
            sum += A[i][i] + A[i][N - 1 - i]  # 🎯 accumulate sum of both diagonals simultaneously
        if N & 1:
            sum -= A[N // 2][N // 2]          # ⭐️ subtract middle element once if it was added twice
        return sum
