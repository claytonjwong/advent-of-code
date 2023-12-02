#
# 933. Number of Recent Calls
#
# Q: https://leetcode.com/problems/number-of-recent-calls/
# A: https://leetcode.com/problems/number-of-recent-calls/discuss/189233/Javascript-Python3-C%2B%2B-Queue-solutions
#

from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()
    def ping(self, t: int) -> int:
        q = self.q
        while len(q) and q[0] < t - 3000:
            q.popleft()
        q.append(t)
        return len(q)
