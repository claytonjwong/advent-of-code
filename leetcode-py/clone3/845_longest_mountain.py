#
# 845. Longest Mountain in Array
#
# Q: https://leetcode.com/problems/longest-mountain-in-array/
# A: https://leetcode.com/problems/longest-mountain-in-array/discuss/135623/Kt-Js-Py3-Cpp-Mountain-Peak
#

from typing import List

class Solution:
    def longestMountain(self, A: List[int], best = 0) -> int:
        N = len(A)
        for k in range(1, N - 1):
            i = k
            j = k
            while 0 <= i - 1 and A[i - 1] < A[i]: i -= 1
            while j + 1 < N  and A[j] > A[j + 1]: j += 1
            if i < k < j:
                best = max(best, j - i + 1)  # +1 for i..j inclusive
        return best
