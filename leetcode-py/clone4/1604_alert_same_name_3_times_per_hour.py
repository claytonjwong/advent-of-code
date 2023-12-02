#
# 1604. Alert Using Same Key-Card Three or More Times in a One Hour Period
#
# Q: https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/
# A: https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/discuss/876799/Javascript-Python3-C%2B%2B-Map-%2B-Queue
#

from typing import List
from collections import deque

class Solution:
    def alertNames(self, names: List[str], times: List[str]) -> List[str]:
        m = {}
        alerts = []
        minutes = lambda time: int(time.split(':')[0]) * 60 + int(time.split(':')[1])
        for name, time in zip(names, times):
            if name not in m:
                m[name] = deque()
            m[name].append(minutes(time))
        for name, times in m.items():
            q = deque()
            for time in sorted(times):
                while len(q) and q[0] + 60 < time:
                    q.popleft()
                q.append(time)
                if 3 <= len(q):
                    alerts.append(name)
                    break
        return sorted(alerts)
