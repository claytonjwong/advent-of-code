#
# 1025. Divisor Game
#
# A: https://leetcode.com/problems/divisor-game/
# Q: https://leetcode.com/problems/divisor-game/discuss/292472/C%2B%2B-solutions%3A-Top-Down-and-Bottom-Up
#

import math

# brute-force
class Solution:
    def divisorGame(self, N: int) -> bool:
        def go(i):
            if i == 1:           # 🛑 base case
                return False
            for j in range(floor(sqrt(i)), 0, -1):
                if not (i % j) and not go(i - j):
                    return True  # 🎯  I win if I play j and you lose
            return False
        return go(N)

# memo
class Solution:
    def divisorGame(self, N: int) -> bool:
        m = [None] * (N + 1)
        def go(i):
            if m[i] != None:     # 🤔 memo
                return m[i]
            if i == 1:           # 🛑 base case
                m[i] = False
                return False
            for j in range(floor(sqrt(i)), 0, -1):
                if not (i % j) and not go(i - j):
                    m[i] = True
                    return True  # 🎯  I win if I play j and you lose
            m[i] = False
            return False
        return go(N)

# bottom-up
class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False] * (N + 1)    # 🤔 memo with implicit 🛑 base case: dp[1] = false
        for i in range(2, N + 1):
            for j in range(floor(sqrt(i)), 0, -1):
                if not (i % j) and not dp[i - j]:
                    dp[i] = True  # 🎯  I win if I play j and you lose
        return dp[N]
