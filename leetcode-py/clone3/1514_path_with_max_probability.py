#
# 1514. Path with Maximum Probability
#
# Q: https://leetcode.com/problems/path-with-maximum-probability/
# A: https://leetcode.com/problems/path-with-maximum-probability/discuss/740901/Javascript-and-C%2B%2B-solutions
#

# Bellman-Ford
class Solution:
    def maxProbability(self, N: int, E: List[List[int]], A: List[float], s: int, t: int) -> float:
        dist = [0] * N;
        dist[s] = 1
        for _ in range(N - 1): # ⭐️ relax edges N - 1 times
            for i, [u, v] in enumerate(E):
                w = A[i]
                dist[u] = max(dist[u], dist[v] * w)
                dist[v] = max(dist[v], dist[u] * w)
        return dist[t]

# SPFA
class Solution:
    def maxProbability(self, N: int, E: List[List[int]], A: List[float], s: int, t: int) -> float:
        adj = list(map(lambda _: [], [None] * N))
        for i, [u, v] in enumerate(E):
            w = A[i]
            adj[u].append([ v, w ])
            adj[v].append([ u, w ])
        dist = [0] * N;
        dist[s] = 1
        q = collections.deque([s])
        while len(q):
            u = q.popleft()
            for [v, w] in adj[u]:
                if dist[v] < dist[u] * w:
                    dist[v] = dist[u] * w # ⭐️ cherry pick v for subsequent edges under consideration to be relaxed
                    q.append(v)
        return dist[t]
