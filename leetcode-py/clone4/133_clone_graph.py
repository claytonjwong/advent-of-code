#
# 133. Clone Graph
#
# Q: https://leetcode.com/problems/clone-graph/
# A: https://leetcode.com/problems/clone-graph/discuss/613748/Kt-Js-Py3-Cpp-DFS-%2B-BFS-via-Map
#

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

# DFS
class Solution:
    def cloneGraph(self, cur: 'Node', m = {}) -> 'Node':
        if not cur:
            return None
        if cur.val in m:
            return m[cur.val]
        m[cur.val] = Node(cur.val)
        for adj in cur.neighbors:
            m[cur.val].neighbors.append(self.cloneGraph(adj, m))
        return m[cur.val]

# BFS
class Solution:
    def cloneGraph(self, start: 'Node') -> 'Node':
        if not start:
            return None
        m = {}
        q = deque([ start ])
        seen = set([ start.val ])
        while q:
            cur = q.popleft()
            m[cur.val] = m[cur.val] if cur.val in m else Node(cur.val)
            for adj in cur.neighbors:
                m[adj.val] = m[adj.val] if adj.val in m else Node(adj.val)
                m[cur.val].neighbors.append(m[adj.val])
                if adj.val not in seen:
                    q.append(adj)
                    seen.add(adj.val)
        return m[start.val]
