#
# 1561. Maximum Number of Coins You Can Get
#
# Q: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
# A: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/discuss/806726/Javascript-Python3-C%2B%2B-Greedy-solutions
#

from typing import List

class Solution:
    def maxCoins(self, A: List[int], ans = 0) -> int:
        A.sort()
        N = len(A)
        K = N // 3
        i = N - 2
        while K:
            ans += A[i]
            i -= 2
            K -= 1
        return ans
