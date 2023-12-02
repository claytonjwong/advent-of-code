#
# 1615. Maximal Network Rank
#
# Q: https://leetcode.com/problems/maximal-network-rank/
# A: https://leetcode.com/problems/maximal-network-rank/discuss/888884/Kt-Js-Py3-Cpp-Brute-Force
#

from typing import List

class Solution:
    def maximalNetworkRank(self, N: int, E: List[List[int]], best = 0) -> int:
        adj = {v: set() for v in range(N)}
        degree = lambda v: len(adj[v])
        for [u, v] in E:
            adj[u].add(v)
            adj[v].add(u)
        for i in range(N):
            for j in range(i + 1, N):
                best = max(best, degree(i) + degree(j) - (j in adj[i]))
        return best
