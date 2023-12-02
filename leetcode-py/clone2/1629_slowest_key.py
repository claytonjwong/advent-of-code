#
# 1629. Slowest Key
#
# Q: https://leetcode.com/problems/slowest-key/
# A: https://leetcode.com/problems/slowest-key/discuss/909815/Kt-Js-Py3-Cpp-Best-Time
#

from typing import List

class Solution:
    def slowestKey(self, A: List[int], keys: str, best = -1, ans = '') -> str:
        for i, key in enumerate(keys):
            time = A[i] - A[i - 1] if 0 < i else A[i]
            if best < time or (best == time and ans < key):
                best = time
                ans = key
        return ans
