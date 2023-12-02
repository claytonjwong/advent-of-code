#
# 941. Valid Mountain Array
#
# Q: https://leetcode.com/problems/valid-mountain-array/
# A: https://leetcode.com/problems/valid-mountain-array/discuss/739686/Kt-Js-Py3-Cpp-Climb-Mountain-to-Find-Peak
#

from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        N = len(A)
        i = 0
        j = N - 1
        while i + 1 < N  and A[i] < A[i + 1]: i += 1  # 👉 climb from left-to-right
        while 0 <= j - 1 and A[j - 1] > A[j]: j -= 1  # 👈 climb from right-to-left
        return 0 < i and i == j and j < N - 1         # 🎯 mountain peak
