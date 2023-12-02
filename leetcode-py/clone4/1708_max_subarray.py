#
# 1708. Largest Subarray Length K
#
# Q: https://leetcode.com/problems/largest-subarray-length-k/
# A: https://leetcode.com/problems/largest-subarray-length-k/discuss/1007617/Kt-Js-Py3-Cpp-Sliding-Window
#

from typing import List
from collections import deque

class Solution:
    def largestSubarray(self, A: List[int], K: int) -> List[int]:
        cand = deque(A[:K])
        best = cand.copy()
        for i in range(K, len(A)):
            cand.popleft(); cand.append(A[i])
            if best < cand:
                best = cand.copy()
        return best
