#
# 799. Champagne Tower
#
# Q: https://leetcode.com/problems/champagne-tower/
# A: https://leetcode.com/problems/champagne-tower/discuss/118694/Kt-Js-Py3-Cpp-The-ART-of-Dynamic-Programming
#

# top-down with memo
class Solution:
    def champagneTower(self, K: int, M: int, N: int) -> float:
        m = {}
        def go(i, j):
            key = f'{i},{j}'
            if key in m:
                return m[key]          # 🤔 memo
            elif not i and not j:
                m[key] = K             # 🛑 base case: glass at row 0 column 0 has K poured through it
            elif not i or j < 0:
                m[key] = 0.0           # 🚫 non-existent parent glass has 0.0 poured through it
            else:
                # ⭐️ each parent glass above-and-to-the-(L)eft/(R)ight either overflow when the amount poured exceeds 1.0 xor do *not* overflow when the amount poured does *not* exceed 1.0
                # 💎 -1.0 since parent glass above consumes at-most 1.0 of the pour and div 2 when overflow occurs, because half overflows on each side of the parent glass
                L = go(i - 1, j - 1)
                R = go(i - 1, j)
                m[key] = ((L - 1.0) / 2 if 1.0 <= L else 0.0) + ((R - 1.0) / 2 if 1.0 <= R else 0.0)
            return m[key]
        go(M, max(M, N))               # 🌟 since the glasses above-and-to-the-right potentially contribute to the amount poured to M, N we choose N to be the maximum of M, N
        return min(go(M, N), 1.0)

# bottom-up
class Solution:
    def champagneTower(self, K: int, M: int, N: int) -> float:
        dp = [[0] * (N + 2) for _ in range(M + 1)]
        dp[0][0] = K
        for i in range(M):
            for j in range(N + 1):
                if dp[i][j] <= 1.0:  # no overflow
                    continue
                half = (dp[i][j] - 1.0) / 2  # -1.0 to fill cup i,j
                dp[i + 1][j]     += half
                dp[i + 1][j + 1] += half
        return min(dp[M][N], 1.0)

# memory optimized
class Solution:
    def champagneTower(self, K: int, M: int, N: int) -> float:
        pre = [0.0] * (N + 2)
        pre[0] = K
        for _ in range(M):
            cur = [0.0] * (N + 2)
            for j in range(N + 1):
                if pre[j] <= 1.0:  # no overflow
                    continue
                half = (pre[j] - 1.0) / 2  # -1.0 to fill cup i,j
                cur[j]     += half
                cur[j + 1] += half
            pre, cur = cur, pre
        return min(pre[N], 1.0)
