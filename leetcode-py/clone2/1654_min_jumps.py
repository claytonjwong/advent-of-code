#
# 1654. Minimum Jumps to Reach Home
#
# Q: https://leetcode.com/problems/minimum-jumps-to-reach-home/
# A: https://leetcode.com/problems/minimum-jumps-to-reach-home/discuss/935386/Kt-Js-Py3-Cpp-BFS-%2B-DFS-solutions
#

from typing import List
from collections import deque

# BFS
class Solution:
    def minimumJumps(self, A: List[int], R: int, L: int, T: int) -> int:
        forbidden = set(A)
        def markSeen(i, backwards):
            key = f'{i},{backwards}'
            if key in seen:
                return False
            seen.add(key)
            return True
        ok = lambda i, backwards: 0 <= i < 4000 and i not in forbidden and markSeen(i, backwards)
        q = deque([[ 0, False, 0 ]])
        seen = set([ '0,False' ])
        while q:
            i, backwards, steps = q.popleft()
            if i == T:
                return steps
            if ok(i + R, False):
                q.append([ i + R, False, steps + 1 ])
            if not backwards and ok(i - L, True):
                q.append([ i - L, True, steps + 1 ])
        return -1

# DFS
class Solution:
    def minimumJumps(self, A: List[int], R: int, L: int, T: int, best = float('inf')) -> int:
        forbidden = set(A)
        seen = set()
        def go(i = 0, steps = 0, backwards = False):
            nonlocal best
            if i in forbidden:                # 🚫 forbidden
                return
            key = f'{i},{backwards}'
            if key in seen:                   # 👀 seen
                return
            seen.add(key)
            if i == T:
                best = min(best, steps)       # 🎯 minimum steps to reach target
                return
            if i < 0 or 4000 < i:             # 🛑 out of bounds
                return
            go(i + R, steps + 1, False)       # 🚀 DFS explore 👉 to-the-right
            if not backwards:
                go(i - L, steps + 1, True)    # 🚀 DFS explore 👈 to-the-left
        go()
        return best if best < float('inf') else -1
