#
# 673. Number of Longest Increasing Subsequence
#
# Q: https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# A: https://leetcode.com/problems/number-of-longest-increasing-subsequence/discuss/916696/Kt-Js-Py3-Cpp-The-ART-of-Dynamic-Programming
#

from typing import List

class Solution:
    def findNumberOfLIS(self, A: List[int], length = 0, best = 0) -> int:
        N = len(A)
        dp = [1] * N
        cnt = [1] * N
        for j in range(0, N):
            for i in range(0, j):
                if A[i] < A[j]:
                    if dp[j] < 1 + dp[i]:
                        dp[j] = 1 + dp[i]
                        cnt[j] = 0
                    if dp[j] == 1 + dp[i]:
                        cnt[j] += cnt[i]
            if length < dp[j]:
                length = dp[j]
                best = 0
            if length == dp[j]:
                best += cnt[j]
        return best
