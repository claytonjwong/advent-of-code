#
# Rank            Name             Score    Finish Time    Q1 (3)     Q2 (4)     Q3 (6)    Q4 (7)
# 2885 / 15080    claytonjwong     7        0:22:12        0:14:46    0:22:12
#

from typing import List

#
# 1560. Most Visited Sector in a Circular Track
#
# Q: https://leetcode.com/problems/most-visited-sector-in-a-circular-track/
# A: https://leetcode.com/problems/most-visited-sector-in-a-circular-track/discuss/806721/Javascript-Python3-C%2B%2B-Brute-Force-Count
#
class Solution:
    def mostVisited(self, N: int, A: List[int]) -> List[int]:
        A = [j - 1 for j in A]  # 💎 -1 for 0-based indexing
        cnt = [0] * N
        i = A[0]
        cnt[i] = 1
        for j in A:
            while i != j:
                i = 0 if i + 1 == N else i + 1  # ⭐️ i wraps-around at N
                cnt[i] += 1
        best = max(cnt)
        return [i + 1 for i, n in enumerate(cnt) if n == best]  # 💎 +1 for 1-based indexing

#
# 1561. Maximum Number of Coins You Can Get
#
# Q: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
# A: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/discuss/806726/Javascript-Python3-C%2B%2B-Greedy-solutions
#
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
