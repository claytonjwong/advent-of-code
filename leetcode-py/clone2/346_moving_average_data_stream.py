#
# 346. Moving Average from Data Stream
#
# Q: https://leetcode.com/problems/moving-average-from-data-stream/
# A: https://leetcode.com/problems/moving-average-from-data-stream/discuss/125631/Javascript-Python3-C%2B%2B-Queue-solutions
#

import collections

class MovingAverage:
    def __init__(self, N: int):
        self.N = N
        self.sum = 0
        self.q = collections.deque()
    def next(self, x: int) -> float:
        if len(self.q) == self.N:
            self.sum -= self.q.popleft()
        self.sum += x; self.q.append(x)
        return self.sum / len(self.q)
