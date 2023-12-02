#
# 818. Race Car
#
# Q: https://leetcode.com/problems/race-car/
# A: https://leetcode.com/problems/race-car/discuss/124312/Javascript-Python3-C%2B%2B-.-BFS-solutions
#

import collections

class Solution:
    def racecar(self, T: int, depth = 0) -> int:
        q = collections.deque([[ 0, 1 ]])
        seen = set('0,1')
        while True:
            k = len(q)
            while k:
                [pos, vel] = q.popleft()
                if pos == T:
                    return depth  # 🎯 target T found
                cand = []
                if abs(T - (pos + vel) < T):
                    cand.append([ pos + vel, 2 * vel ])
                cand.append([ pos, 1 if vel < 0 else -1 ])
                for pos, vel in cand:
                    if f'{pos},{vel}' not in seen:
                        q.append([ pos, vel ])
                        seen.add(f'{pos},{vel}')
                k -= 1
            depth += 1
        return -1
