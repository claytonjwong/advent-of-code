#
# 1588. Sum of All Odd Length Subarrays
#
# Q: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
# A: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/discuss/854147/Javascript-Python3-C%2B%2B-Prefix-Sums
#

from typing import List

class Solution:
    def sumOddLengthSubarrays(self, A: List[int], total = 0) -> int:
        N = len(A)
        S = [0] * (N + 1)
        for i in range(1, N + 1):
            S[i] = S[i - 1] + A[i - 1]          # 🧩 prefix sums S
        for i in range(N):
            for j in range(1, N + 1 - i, 2):    # 👀 odd length j: 1, 3, 5, ...
                total += S[i + j] - S[i]
        return total                            # 🎯 sum of odd length subarrays
