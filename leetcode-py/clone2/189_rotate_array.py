#
# 189. Rotate Array
#
# Q: https://leetcode.com/problems/rotate-array/
# A: https://leetcode.com/problems/rotate-array/discuss/895736/Kt-Js-Py3-Cpp-K-Rotations
#

from typing import List

class Solution:
    def rotate(self, A: List[int], K: int) -> None:
        while K:
            last = A[-1]
            for i in range(len(A) - 1, 0, -1):
                A[i] = A[i - 1]
            A[0] = last
            K -= 1
