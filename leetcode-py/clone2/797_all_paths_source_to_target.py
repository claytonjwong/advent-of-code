#
# 797. All Paths From Source to Target
#
# Q: https://leetcode.com/problems/all-paths-from-source-to-target/
# A: https://leetcode.com/problems/all-paths-from-source-to-target/discuss/752917/Kt-Js-Py3-Cpp-DFS-%2B-BT
#

from typing import List

class Solution:
    def allPathsSourceTarget(self, adj: List[List[int]]) -> List[List[int]]:
        paths = []
        N = len(adj)
        s = 0
        t = N - 1
        def go(path):
            u = path[-1]
            if u == t:
                paths.append(path[:])            # 🎯 target t reached
            else:
                for v in adj[u]: go(path + [v])  # 🚀 explore edge u -> v with implicit ✅ 👀 forward-tracking + 🚫 👀 back-tracking
        go([s])
        return paths
