#
# 1539. Kth Missing Positive Number
#
# Q: https://leetcode.com/problems/kth-missing-positive-number/
# A: https://leetcode.com/problems/kth-missing-positive-number/discuss/780016/Kt-Js-Py3-Cpp-Seen-Set-%2B-Concise
#

from typing import List

# seen
class Solution:
    def findKthPositive(self, A: List[int], K: int) -> int:
        seen = set(A)
        i = 1
        while True:
            if not i in seen:
                K -= 1
                if K == 0:
                    return i
            i += 1

# concise
class Solution:
    def findKthPositive(self, A: List[int], k: int) -> int:
        i = 0
        x = 0
        while k and i < len(A):
            x += 1
            if x == A[i]:
                i += 1
            else:
                k -= 1
        return x + k
