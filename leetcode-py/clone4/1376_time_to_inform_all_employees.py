#
# 1376. Time Needed to Inform All Employees
#
# Q: https://leetcode.com/problems/time-needed-to-inform-all-employees/
# A: https://leetcode.com/problems/time-needed-to-inform-all-employees/discuss/534379/Javascript-and-C%2B%2B-solutions
#

# DFS
class Solution:
    def numOfMinutes(self, N: int, root: int, A: List[int], cost: List[int]) -> int:
        adj = list(map(lambda _: [], [None] * N))
        for v, u in enumerate(A): adj[u].append(v) if -1 < u else None
        go = lambda u: cost[u] + max([go(v) for v in adj[u]]) if len(adj[u]) else 0
        return go(root)

# BFS
class Solution:
    def numOfMinutes(self, N: int, root: int, A: List[int], cost: List[int], ans = 0) -> int:
        adj = list(map(lambda _: [], [None] * N))
        for v, u in enumerate(A):
            adj[u].append(v) if -1 < u else None
        dist = [0] * N
        q = collections.deque([ root ])
        while q:
            u = q.popleft()
            for v in adj[u]:
                dist[v] = dist[u] + cost[u]
                ans = max(ans, dist[v])
                q.append(v)
        return ans
