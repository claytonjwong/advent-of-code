#
# https://leetcode.com/contest/biweekly-contest-33/ranking
#
# Rank            Name            Score    Finish Time    Q1 (3)     Q2 (4)    Q3 (5)    Q4 (6)
# 4704 / 11366    claytonjwong    7        0:37:57        0:08:07    0:37:57
#

from typing import List


#
# 1556. Thousand Separator
#
# Q: https://leetcode.com/problems/thousand-separator/
# A: https://leetcode.com/problems/thousand-separator/discuss/805674/Javascript-Python3-C%2B%2B-1-Liners
#

class Solution:
    def thousandSeparator(self, n: int) -> str:
        return str(n) if n < 1000 else self.thousandSeparator(n // 1000) + '.' + str(n % 1000).zfill(3)


#
# 1557. Minimum Number of Vertices to Reach All Nodes
#
# Q: https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
# A: https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/discuss/805698/Javascript-Python3-C%2B%2B-In-Degree-0
#

class Solution:
    def findSmallestSetOfVertices(self, N: int, E: List[List[int]]) -> List[int]:
        deg = [0] * N
        for [_, tail] in E:
            deg[tail] += 1
        return list(filter(lambda x: -1 < x, [-1 if x else i for i, x in enumerate(deg)]))

# simplified
class Solution:
    def findSmallestSetOfVertices(self, N: int, E: List[List[int]]) -> List[int]:
        all = set([i for i in range(N)])
        for [_, tail] in E:
            if tail in all:
                all.remove(tail)
        return all
