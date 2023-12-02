#
# 1560. Most Visited Sector in a Circular Track
#
# Q: https://leetcode.com/problems/most-visited-sector-in-a-circular-track/
# A: https://leetcode.com/problems/most-visited-sector-in-a-circular-track/discuss/806721/Javascript-Python3-C%2B%2B-Brute-Force-Count
#

from typing import List

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
