#
# 1625. Lexicographically Smallest String After Applying Operations
#
# Q: https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/
# A: https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/discuss/903526/Kt-Js-Py3-Cpp-Brute-Force-via-DFS-%2B-BFS
#

from collections import deque

# DFS
class Solution:
    def findLexSmallestString(self, s: str, amount: int, pivot: int) -> str:
        best = s
        seen = set([ s ])
        def go(s):
            nonlocal best
            if best > s:
                best = s
            increment = ''.join([str((int(c) + amount) % 10) if i & 1 else c for i, c in enumerate(s)])
            if increment not in seen:
                seen.add(increment); go(increment)
            rotate = s[pivot:] + s[:pivot]
            if rotate not in seen:
                seen.add(rotate); go(rotate)
        go(s)
        return best

# BFS
class Solution:
    def findLexSmallestString(self, s: str, amount: int, pivot: int) -> str:
        best = s
        seen = set([ s ])
        q = deque([ s ])
        while q:
            cur = q.popleft()
            if best > cur:
                best = cur
            increment = ''.join([str((int(c) + amount) % 10) if i & 1 else c for i, c in enumerate(cur)])
            if increment not in seen:
                seen.add(increment); q.append(increment)
            rotate = cur[pivot:] + cur[:pivot]
            if rotate not in seen:
                seen.add(rotate); q.append(rotate)
        return best
