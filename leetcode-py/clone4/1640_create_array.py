#
# 1640. Check Array Formation Through Concatenation
#
# Q: https://leetcode.com/problems/check-array-formation-through-concatenation/
# A: https://leetcode.com/problems/check-array-formation-through-concatenation/discuss/919391/Kt-Js-Py3-Cpp-Do-we-%22have%22-what-we-%22need%22
#

from typing import List
from collections import deque

# queue
class Solution:
    def canFormArray(self, need: List[int], have: List[List[int]]) -> bool:
        q = deque()
        for x in need:
            if q:
                if x != q[0]:
                    return False
                q.popleft()
                continue
            found = False
            for piece in have:
                if x == piece[0]:
                    found = True
                    q.extend(piece[1:])
                    break
            if not found:
                return False
        return True

# make
class Solution:
    def canFormArray(self, need: List[int], have: List[List[int]]) -> bool:
        m = {A[0]: i for i, A in enumerate(have)}
        make = []
        i = 0
        N = len(need)
        while i < N:
            if need[i] not in m:
                return False
            j = m[need[i]]
            make.extend(have[j].copy())
            i += len(have[j])
        return need == make
