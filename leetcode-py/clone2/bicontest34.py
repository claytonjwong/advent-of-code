#
# Biweekly Contest 34 (3651 / 10140)
#
# Ranking:     https://leetcode.com/contest/biweekly-contest-34/ranking
# Screenshare: https://www.youtube.com/watch?v=WY60iZuPyCk
#
# Rank            Name            Score    Finish Time     Q1 (3)      Q2 (4)       Q3 (5)      Q4 (6)
# 3651 / 10140    claytonjwong    7        1:27:15         0:02:12     1:12:15 *3
#

from typing import List

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


#
# 1573. Number of Ways to Split a String
#
# Q: https://leetcode.com/problems/number-of-ways-to-split-a-string/
# A: https://leetcode.com/problems/number-of-ways-to-split-a-string/discuss/830433/Javascript-Python3-C%2B%2B-solutions
#

class Solution:
    def numWays(self, S: str, MOD = int(1e9 + 7)) -> int:
        N = len(S)
        cnt = len([c for c in S if c == '1'])
        # case 1: all zeros, return the sum of the series for the cardinality of S minus 1
        if not cnt:
            return (N - 2) * (N - 1) // 2 % MOD
        # case 2: cannot evenly divide the ones into 3 equal paritions
        if cnt % 3:
            return 0
        # case 3: return the product of the first and second accumulated "gaps of zeros" between each parition of equal ones
        K = cnt // 3
        first = 0
        second = 0
        ones = 0
        for i in range(N):
            if S[i] == '1':
                ones += 1
            if ones == 1 * K and S[i] == '0': first +=1
            if ones == 2 * K and S[i] == '0': second += 1
        return (first + 1) * (second + 1) % MOD  # ⭐️ +1 for "gaps of zeros" from i..j inclusive
