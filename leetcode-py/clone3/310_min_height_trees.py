#
# 310. Minimum Height Trees
#
# Q: https://leetcode.com/problems/minimum-height-trees/
# A: https://leetcode.com/problems/minimum-height-trees/discuss/118585/Kt-Js-Py3-Cpp-BFS-Prune-Leaves
#

from typing import List
from collections import deque

class Solution:
    def findMinHeightTrees(self, N: int, E: List[List[int]]) -> List[int]:
        if not len(E):
            return [ 0 ]
        adj = { i: set() for i in range(N) }
        for u, v in E:
            adj[u].add(v)
            adj[v].add(u)
        isLeaf = lambda v: len(adj[v]) == 1
        q = deque([ v for v in range(N) if isLeaf(v) ])
        while 2 < N:
            k = len(q); N -= k
            while k:
                u = q.popleft()
                for v in adj[u]:
                    adj[v].remove(u)
                    if isLeaf(v):
                        q.append(v)
                k -= 1
        return list(q)
