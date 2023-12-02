#
# 1656. Design an Ordered Stream
#
# Q: https://leetcode.com/problems/design-an-ordered-stream/
# A: https://leetcode.com/problems/design-an-ordered-stream/discuss/947961/Kt-Js-Py3-Cpp-Array
#

from typing import List

class OrderedStream:
    def __init__(self, N: int):
        self.i = 0
        self.N = N
        self.A = [''] * N
    def insert(self, k: int, value: str) -> List[str]:
        res = []
        self.A[k - 1] = value  # -1 for 0-based indexing
        while self.i < self.N and len(self.A[self.i]):
            res.append(self.A[self.i])
            self.i += 1
        return res
