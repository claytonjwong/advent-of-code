#
# 1046. Last Stone Weight
#
# Q: https://leetcode.com/problems/last-stone-weight/
# A: https://leetcode.com/problems/last-stone-weight/discuss/577600/Javascript-Python3-C%2B%2B-.-.-Priority-Queue
#

from heapq import heapify, heappush, heappop
from typing import List

class Solution:
    def lastStoneWeight(self, A: List[int]) -> int:
        q = [-x for x in A]
        heapify(q)
        while 1 < len(q):
            a = heappop(q)
            b = heappop(q)
            heappush(q, -abs(a - b))
        return -heappop(q)
