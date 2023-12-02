#
# 767. Reorganize String
#
# Q: https://leetcode.com/problems/reorganize-string/
# A: https://leetcode.com/problems/reorganize-string/discuss/113426/Js-Py3-Cpp-Priority-Queue
#

from collections import Counter
from heapq import heappush, heappop

class Solution:
    def reorganizeString(self, s: str) -> str:
        q = []
        t = []
        m = Counter(s)
        for c, cnt in m.items():
            heappush(q, [-cnt, c])
        while 1 < len(q):
            cnt_a, a = heappop(q)
            cnt_b, b = heappop(q)
            t.append(a); cnt_a += 1
            t.append(b); cnt_b += 1
            if cnt_a: heappush(q, [cnt_a, a])
            if cnt_b: heappush(q, [cnt_b, b])
        if len(q):
            _, a = heappop(q)
            t.append(a)
        return ''.join(t) if len(s) == len(t) else ''
