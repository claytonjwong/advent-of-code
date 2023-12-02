#
# 1578. Minimum Deletion Cost to Avoid Repeating Letters
#
# Q: https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/
# A: https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/discuss/836954/Javascript-Python3-C%2B%2B-Greedy
#

from typing import List

class Solution:
    def minCost(self, S: str, cost: List[int], total = 0) -> int:
        N = len(S)
        i = 0
        while i < N:
            j = i
            run = cost[j]
            big = cost[j]
            while j + 1 < N and S[j] == S[j + 1]:  # 🚌 accumulate current "run" costs and track the maximum cost
                j += 1
                run += cost[j]
                big = max(big, cost[j])
            total += run - big                     # 🎯 greedily consume K - 1 minimal values for each "run" of length K if 1 < K
            i = j + 1
        return total
