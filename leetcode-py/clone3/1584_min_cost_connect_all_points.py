#
# 1584. Min Cost to Connect All Points
#
# Q: https://leetcode.com/problems/min-cost-to-connect-all-points/
# A: https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/850003/Javascript-Python3-C%2B%2B-Kruskal's-MST
#

from typing import List

# kruskal
class Solution:
    def minCostConnectPoints(self, A: List[List[int]]) -> int:
        N = len(A)
        P = [i for i in range(N)]                        # 🙂 parent representatives of N disjoint sets
        E = []
        for u in range(N):
            x1, y1 = A[u]
            for v in range(u + 1, N):
                x2, y2 = A[v]
                w = abs(x1 - x2) + abs(y1 - y2)
                E.append([ u, v, w ])                    # 🗺 edge u, v with weight w 💰
        E.sort(key = lambda edge: edge[2])               # ⭐️ sort edges by weight w 💰
        def find(x):
            P[x] = P[x] if P[x] == x else find(P[x])
            return P[x]
        def union(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return False
            P[a] = b                                     # 🎲 arbitrary choice
            return True
        return sum([w for u, v, w in E if union(u, v)])  # 🎯 sum of minimum edge weights w 💰 to construct Kruskal's MST 🌲

# prim
class Solution:
    def minCostConnectPoints(self, A: List[List[int]], total = 0) -> int:
        N = len(A)
        cand = set([i for i in range(1, N)])
        E = [[float('inf')] * N for _ in range(N)]
        for u in range(N):
            x1, y1 = A[u]
            for v in range(u + 1, N):
                x2, y2 = A[v]
                cost = abs(x1 - x2) + abs(y1 - y2)
                E[u][v] = cost
                E[v][u] = cost
        s = 0
        q = []
        best = [float('inf')] * N
        for v in range(1, N):
            if best[v] > E[s][v]:
                best[v] = E[s][v]
                heappush(q, [best[v], v])
        while len(cand):
            cost, u = heappop(q)
            if u not in cand:
                continue
            cand.remove(u)
            total += cost
            for v in range(N):
                if v not in cand:
                    continue
                if best[v] > E[u][v]:
                    best[v] = E[u][v]
                    heappush(q, [best[v], v])
        return total
