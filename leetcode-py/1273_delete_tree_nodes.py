#
# 1273. Delete Tree Nodes
#
# Q: https://leetcode.com/problems/delete-tree-nodes/
# A: https://leetcode.com/problems/delete-tree-nodes/discuss/476958/Javascript-Python3-C%2B%2B-BFS-Prune-Leaves
#

from typing import List
from collections import deque

class Solution:
    def deleteTreeNodes(self, N: int, P: List[int], total: List[int], pruned = 0) -> int:
        degree = [0] * N
        for parent in P:
            if parent != -1:
                degree[parent] += 1
        q = deque()
        [q.append(i) for i, x in enumerate(degree) if not x]
        nodes = [1] * N
        while len(q):
            child = q.popleft()
            parent = P[child]
            if not total[child]:
                pruned += nodes[child]
            elif parent != -1:
                nodes[parent] += nodes[child]
                total[parent] += total[child]
            if parent != -1:
                degree[parent] -= 1
                if not degree[parent]:
                    q.append(parent)
        return N - pruned
