#
# 210. Course Schedule II
#
# Q: https://leetcode.com/problems/course-schedule-ii/
# A: https://leetcode.com/problems/course-schedule-ii/discuss/742411/Javascript-Python3-C%2B%2B-DFS-%2B-BFS-Pruning
#

# BFS pruning
class Solution:
    def findOrder(self, N: int, E: List[List[int]]) -> List[int]:
        ans = []
        adj = { i: set() for i in range(N) } # adjacent children
        cnt = [0] * N                        # incoming edge count
        for [v, u] in E:
            adj[u].add(v)
            cnt[v] += 1
        # ⭐️ bfs pruning of nodes with no incoming edge count
        q = collections.deque([i for i, incoming in enumerate(cnt) if not incoming])
        while q:
            u = q.popleft();
            ans.append(u) # 🎯 bfs pruned
            for v in adj[u]:
                cnt[v] -= 1
                if not cnt[v]:
                    q.append(v)
        return ans if len(ans) == N else []

# DFS pruning
class Solution:
    def go(self, u: int) -> bool:
        if u in self.visited:  # 🤔 🔍 already visited
            return True
        if u in self.visiting: # ❌ cycle
            return False
        self.visiting.add(u)    # 👀 ephemeral visiting: ✅ forward-tracking
        for v in self.adj[u]:
            if not self.go(v):
                return False
        self.visiting.remove(u) # 👀 ephemeral visiting: 🚫 back-tracking
        self.visited.add(u) # 🤔 📌 permanent visited
        self.ans.append(u) # 🎯 the answer is dfs pruned in reverse order, ie. as the recusive stack unwinds
        return True
    def findOrder(self, N: int, E: List[List[int]]) -> List[int]:
        self.ans = []
        self.visiting, self.visited = set(), set()
        self.adj = { i: set() for i in range(N) } # adjacent children
        for [v, u] in E:
            self.adj[u].add(v)
        for i in range(N):
            if not self.go(i):
                return []
        return self.ans[::-1] # 🎯 the answer is dfs constructed in reverse
