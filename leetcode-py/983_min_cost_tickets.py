#
# 983. Minimum Cost For Tickets
#
# Q: https://leetcode.com/problems/minimum-cost-for-tickets/
# A: https://leetcode.com/problems/minimum-cost-for-tickets/discuss/811237/Javascript-Python3-C%2B%2B-Top-Down-%2B-Bottom-Up
#

from typing import List

# top-down
class Solution:
    def mincostTickets(self, A: List[int], cost: List[int]) -> int:
        days = [1, 7, 30]
        N = len(A)
        def go(i = 0, day = 0):
            while i < N and A[i] < day:
                i += 1
            if i == N:
                return 0        # 🛑 base case
            best = float('inf')
            for k in range(3):
                best = min(best, cost[k] + go(i, A[i] + days[k]))   # 🎯 min cost
            return best
        return go()

# top-down memo
class Solution:
    def mincostTickets(self, A: List[int], cost: List[int], days = [1, 7, 30]) -> int:
        m = {}
        N = len(A)
        def go(i = 0, day = 0):
            while i < N and A[i] < day:
                i += 1
            if i == N:
                return 0        # 🛑 base case
            if i in m:
                return m[i]     # 🤔 memo
            m[i] = float('inf')
            for k in range(3):
                m[i] = min(m[i], cost[k] + go(i, A[i] + days[k]))   # 🎯 min cost
            return m[i]
        return go()

# bottom-up
class Solution:
    def mincostTickets(self, A: List[int], cost: List[int], days = [1, 7, 30]) -> int:
        N = len(A)
        dp = [float('inf')] * (N + 1)   # 🤔 memo
        dp[N] = 0                       # 🛑 base case
        for i in range(N, -1, -1):
            j = i
            for k in range(3):
                while j < N and A[j] < A[i] + days[k]:
                    j += 1
                dp[i] = min(dp[i], cost[k] + dp[j])   # 🎯 min cost
        return dp[0]
