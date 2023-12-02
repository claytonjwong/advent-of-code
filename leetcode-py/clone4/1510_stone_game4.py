#
# 1510. Stone Game IV
#
# Q: https://leetcode.com/problems/stone-game-iv/
# A: https://leetcode.com/problems/stone-game-iv/discuss/737869/Javascript-Python3-C%2B%2B
#

# top-down
class Solution:
    def go(self, i: int) -> bool:
        if not i:
            return False # 🛑 base case: no stones left
        for j in range(math.floor(math.sqrt(i)), 0, -1): # ⭐️ take each (j * j) stones
            if not self.go(i - (j * j)):
                return True # 🎯 if next player lost, then current player wins
        return False
    def winnerSquareGame(self, N: int) -> bool:
        return self.go(N)

# top-down memo
class Solution:
    def go(self, i: int, m = {}) -> bool:
        if i in m:
            return m[i] # 🤔 memo
        if not i:
            m[i] = False
            return False # 🛑 base case: no stones left
        for j in range(math.floor(math.sqrt(i)), 0, -1): # ⭐️ take each (j * j) stones, 💎 avoid TLE by taking largest (j * j) first
            if not self.go(i - (j * j)):
                m[i] = True
                return True # 🎯 if next player lost, then current player wins
        m[i] = False
        return False
    def winnerSquareGame(self, N: int) -> bool:
        return self.go(N)

# bottom-up
class Solution:
    def winnerSquareGame(self, N: int) -> bool:
        dp = [False] * (N + 1)
        dp[0] = False # 🛑 base case: no stones left
        for i in range(0, N + 1):
            for j in range(math.floor(math.sqrt(i)), 0, -1): # ⭐️ take each (j * j) stones
                if not dp[i - (j * j)]:
                    dp[i] = True # 🎯 if next player lost, then current player wins
        return dp[N]
