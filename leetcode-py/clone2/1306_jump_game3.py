#
# 1306. Jump Game III
#
# Q: https://leetcode.com/problems/jump-game-iii/
# A: https://leetcode.com/problems/jump-game-iii/discuss/464420/Kt-Js-Py3-Cpp-BFS-%2B-DFS
#

from typing import List

# BFS
class Solution:
    def canReach(self, A: List[int], start: int) -> bool:
        seen = set()
        q = deque([start])
        while q:
            i = q.popleft()
            if not A[i]:
                return True
            for j in [i + A[i], i - A[i]]:
                if 0 <= j < len(A) and j not in seen:
                    q.append(j); seen.add(j)
        return False

# DFS
class Solution:
    def canReach(self, A: List[int], start: int) -> bool:
        seen = set()
        def go(i = start):
            if i < 0 or len(A) <= i or i in seen:
                return False
            seen.add(i)
            if not A[i]:
                return True
            return go(i + A[i]) or go(i - A[i])
        return go()
