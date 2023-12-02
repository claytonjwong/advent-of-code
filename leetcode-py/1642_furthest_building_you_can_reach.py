#
# 1642. Furthest Building You Can Reach
#
# Q: https://leetcode.com/problems/furthest-building-you-can-reach/
# A: https://leetcode.com/problems/furthest-building-you-can-reach/discuss/1178012/Greedy%3A-Do-we-HAVE-what-we-NEED
#

from typing import List
from heapq import heappush, heappop

class Solution:
    def furthestBuilding(self, A: List[int], have: int, K: int, best = 0) -> int:
        q = []
        N = len(A)
        for i in range(1, N):
            need = A[i] - A[i - 1]
            if 0 < need:
                heappush(q, need)      # 🤔 remeber K ladders consumption: the amount of bricks we need for the i-th building "hop"
                if K:
                    K -= 1             # 💰 greedily consume all K ladders
                else:
                    need = heappop(q)  # 💰 greedily consume minimal need, ie. do we have the amount of bricks we need for the minimal amount of bricks of a previous i-th building "hop"?
                    if have < need:
                        break
                    have -= need
            best += 1
        return best


A = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2
print(Solution().furthestBuilding(A, bricks, ladders))
