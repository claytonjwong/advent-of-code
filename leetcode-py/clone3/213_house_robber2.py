#
# 213. House Robber II
#
# Q: https://leetcode.com/problems/house-robber-ii/
# A: https://leetcode.com/problems/house-robber-ii/discuss/894504/Kt-Js-Py3-Cpp-The-ART-of-Dynamic-Programming
#

from typing import List

# brute-force
class Solution:
    def rob(self, A: List[int]) -> int:
        N = len(A)
        def go(i, first, last):
            if i == N:                                                      # 🛑 base case
                return 0
            if last + 1 == i or (first and i + 1 == N and 1 < N):           # 🚫 without i-th house (due to adjacent neighbor constraint)
                return go(i + 1, first, last)
            return max(A[i] + go(i + 1, first, i), go(i + 1, first, last))  # ✅ with i-th house xor 🚫 without i-th house
        return max(go(0, True, -123), go(1, False, -123))                   # ✅ with first house xor 🚫 without first house

# top-down memo
class Solution:
    def rob(self, A: List[int]) -> int:
        m = {}
        N = len(A)
        def go(i, first, last):
            key = f'{i},{first},{last}'
            if key in m:                                                          # 🤔 memo
                return m[key]
            if i == N:                                                            # 🛑 base case
                m[key] = 0
            elif last + 1 == i or (first and i + 1 == N and 1 < N):               # 🚫 without i-th house (due to adjacent neighbor constraint)
                m[key] = go(i + 1, first, last)
            else:
                m[key] = max(A[i] + go(i + 1, first, i), go(i + 1, first, last))  # ✅ with i-th house xor 🚫 without i-th house
            return m[key]
        return max(go(0, True, -123), go(1, False, -123))                         # ✅ with first house xor 🚫 without first house

# bottom-up
class Solution:
    def rob(self, A: List[int]) -> int:
        N = len(A)
        if N == 1:                                                # 💎 corner case
            return A[0]
        def best(start):
            dp = [0] * (N + 2)                                    # 🤔 memo + 🛑 base cases (ie. dp[N] = 0 and dp[N + 1] = 0)
            for i in range(N - 1 - (0 if start else 1), -1, -1):
                dp[i] = max(A[i] + dp[i + 2], dp[i + 1])          # ✅ with i-th house xor 🚫 without i-th house
            return dp[start]
        return max(best(0), best(1))                              # ✅ with first house xor 🚫 without first house

# bottom-up memory optimization
class Solution:
    def rob(self, A: List[int]) -> int:
        N = len(A)
        if N == 1:                                                       # 💎 corner case
            return A[0]
        def best(start):
            a, b, c = 0, 0, 0                                            # 🤔 memo + 🛑 base cases (ie. a = 0 and b = 0)
            for i in range(N - 1 - (0 if start else 1), start - 1, -1):
                c = max(A[i] + a, b)                                     # ✅ with i-th house xor 🚫 without i-th house
                a = b; b = c                                             # 👉 slide window
            return c
        return max(best(0), best(1))                                     # ✅ with first house xor 🚫 without first house
