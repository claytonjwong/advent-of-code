#
# 198. House Robber
#
# Q: https://leetcode.com/problems/house-robber/
# A: https://leetcode.com/problems/house-robber/discuss/846461/Javascript-Python3-C%2B%2B-The-ART-of-Dynamic-Programming
#

# brute-force
class Solution:
    def rob(self, A: List[int]) -> int:
        def go(pre = -2, cur = 0):
            if cur == len(A):
                return 0                  # 🛑 base case
            elif pre == cur - 1:
                return go(pre, cur + 1)   # 🚫 without (due to adjacent neighbor constraint)
            else:
                return max(A[cur] + go(cur, cur + 1), go(pre, cur + 1))  # ✅ with or 🚫 without
        return go()

# memo
class Solution:
    def rob(self, A: List[int]) -> int:
        m = {}
        def go(pre = -2, cur = 0):
            key = f'{pre},{cur}'
            if key in m:
                return m[key]               # 🤔 memo
            if cur == len(A):
                m[key] = 0                  # 🛑 base case
            elif pre == cur - 1:
                m[key] = go(pre, cur + 1)   # 🚫 without (due to adjacent neighbor constraint)
            else:
                m[key] = max(A[cur] + go(cur, cur + 1), go(pre, cur + 1))  # ✅ with or 🚫 without
            return m[key]
        return go()

# bottom-up
class Solution:
    def rob(self, A: List[int]) -> int:
        N = len(A)
        dp = [0] * (N + 2)                             # 🤔 memo +2 for 🛑 base cases
        for i in range(N - 1, -1, -1):
            dp[i] = max(A[i] + dp[i + 2], dp[i + 1])   # ✅ with or 🚫 without
        return max(dp[0], dp[1])
