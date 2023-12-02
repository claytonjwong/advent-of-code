#
# 359. Logger Rate Limiter
#
# Q: https://leetcode.com/problems/logger-rate-limiter/
# A: https://leetcode.com/problems/logger-rate-limiter/discuss/473779/Javascript-Python3-C%2B%2B-hash-table
#

class Logger:
    def __init__(self):
        self.m = {}
    def shouldPrintMessage(self, t: int, s: str) -> bool:
        m = self.m
        if not s in m or 10 <= t - m[s]:
            m[s] = t
            return True
        return False
