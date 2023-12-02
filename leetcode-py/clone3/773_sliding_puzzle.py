#
# 773. Sliding Puzzle
#
# Q: https://leetcode.com/problems/sliding-puzzle/
# A: https://leetcode.com/problems/sliding-puzzle/discuss/113694/C%2B%2B-BFS-with-explanation-and-example-(-EASY-to-understand-)
#

from typing import List
from functools import reduce
import collections

class Solution:
    def slidingPuzzle(self, A: List[List[int]], T = '123450', adj = { 0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4] }, depth = 0) -> int:
        key = lambda a: ''.join([str(x) for x in a])
        init = reduce(lambda a, b: a + b, A, [])
        q, seen = collections.deque([ init ]), set([ key(init) ])
        while q:
            k = len(q)
            for _ in range(k):
                cur = q.popleft()
                if key(cur) == T: # 🎯 target T found
                    return depth
                i = cur.index(0)
                for j in adj[i]:
                    next = cur.copy()
                    next[i], next[j] = next[j], next[i] # swap i,j
                    if not key(next) in seen:
                        q.append(next)
                        seen.add(key(next))
            depth += 1
        return -1
