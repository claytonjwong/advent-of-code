#
# 1579. Remove Max Number of Edges to Keep Graph Fully Traversable
#
# Q: https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
# A: https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/discuss/848649/Javascript-Python3-C%2B%2B-Union-Find-%2B-Greedy
#

from typing import List

class Solution:
    def maxNumEdgesToRemove(self, N: int, E: List[List[int]], same = 0) -> int:
        E = [[_, u - 1, v - 1] for _, u, v in E]                    # ⭐️ -1 for 1-based to 0-based indexing
        A = [i for i in range(N)]                                   # 🙂 parent representatives of disjoint sets for Alice
        B = [i for i in range(N)]                                   # 🙂 parent representatives of disjoint sets for Bob
        def find(P, x): P[x] = P[x] if P[x] == x else find(P, P[x]); return P[x]
        def union(P, a, b):
            a = find(P, a)
            b = find(P, b)
            if a == b:
                return 1
            P[a] = b  # arbitrary choice
            return 0
        for type, u, v in E:
            if type == 3: same += union(A, u, v) | union(B, u, v)   # 🥇 first: 🔗 union shared edges for Alice and Bob
        for type, u, v in E:
            if type == 1: same += union(A, u, v)                    # 🥈 second: 🔗 union for Alice
            if type == 2: same += union(B, u, v)                    #            🔗 union for Bob
        # 🎯 is there a single connected component for Alice and Bob?
        # if so, return the accumulated amount of edges which redundantly connect
        # to each same connected component for Alice and Bob
        return same if all(find(A, 0) == find(A, x) for x in A) and all(find(B, 0) == find(B, x) for x in B) else -1
