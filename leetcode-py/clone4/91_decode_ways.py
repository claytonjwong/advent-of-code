#
# 91. Decode Ways
#
# Q: https://leetcode.com/problems/decode-ways/
# A: https://leetcode.com/problems/decode-ways/discuss/117143/Kt-Js-Py3-Cpp-The-ART-of-Dynamic-Programming
#

# top-down
class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        ok = lambda x: 1 <= x <= 26
        def go(i = 0):
            if i == N:
                return 1
            cnt = 0
            one = int(s[i])
            two = int(s[i:i + 2]) if one and i + 2 <= N else 0
            if ok(one): cnt += go(i + 1)
            if ok(two): cnt += go(i + 2)
            return cnt
        return go()

# top-down with memo (concise)
class Solution:
    def numDecodings(self, s: str) -> int:
        m = {}
        N = len(s)
        ok = lambda x: 1 <= x <= 26
        @cache
        def go(i = 0):
            if i == N:
                return 1
            cnt = 0
            one = int(s[i])
            two = int(s[i:i + 2]) if one and i + 2 <= N else 0
            if ok(one): cnt += go(i + 1)
            if ok(two): cnt += go(i + 2)
            return cnt
        return go()

# top-down with memo (verbose)
class Solution:
    def numDecodings(self, s: str) -> int:
        m = {}
        N = len(s)
        ok = lambda x: 1 <= x <= 26
        def go(i = 0):
            if i in m:
                return m[i]
            if i == N:
                return 1
            m[i] = 0
            one = int(s[i])
            two = int(s[i:i + 2]) if one and i + 2 <= N else 0
            if ok(one): m[i] += go(i + 1)
            if ok(two): m[i] += go(i + 2)
            return m[i]
        return go()

# bottom-up
class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [0] * (N + 2)
        dp[N] = 1
        ok = lambda x: 1 <= x <= 26
        for i in range(N - 1, -1, -1):
            one = int(s[i])
            two = int(s[i:i + 2]) if one and i + 2 <= N else 0
            if ok(one): dp[i] += dp[i + 1]
            if ok(two): dp[i] += dp[i + 2]
        return dp[0]

# bottom-up mem-opt
class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        a = 0
        b = 1
        c = 0
        ok = lambda x: 1 <= x <= 26
        for i in range(N - 1, -1, -1):
            one = int(s[i])
            two = int(s[i:i + 2]) if one and i + 2 <= N else 0
            a = 0
            if ok(one): a += b
            if ok(two): a += c
            c = b; b = a
        return a
