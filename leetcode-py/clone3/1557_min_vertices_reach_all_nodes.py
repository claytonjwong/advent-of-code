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
