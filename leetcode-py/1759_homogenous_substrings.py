#
# 1759. Count Number of Homogenous Substrings
#
# Q: https://leetcode.com/problems/count-number-of-homogenous-substrings/
# A: https://leetcode.com/problems/count-number-of-homogenous-substrings/discuss/1064522/Kt-Js-Py3-Cpp-Dynamic-Progamming
#

# verbose
class Solution:
    def countHomogenous(self, s: str, mod = int(1e9 + 7), ans = 0) -> int:
        N = len(s)
        dp = [1] * N
        for i, c in enumerate(s):
            if i and s[i - 1] == s[i]:
                dp[i] = (dp[i] + dp[i - 1]) % mod
            ans = (ans + dp[i]) % mod
        return ans

# concise
class Solution:
    def countHomogenous(self, s: str, mod = int(1e9 + 7), pre = 1, cur = 1, last = '\0', ans = 0) -> int:
        for c in s:
            cur = (1 + pre) if c == last else 1
            ans = (ans + cur) % mod
            pre = cur; last = c
        return ans
