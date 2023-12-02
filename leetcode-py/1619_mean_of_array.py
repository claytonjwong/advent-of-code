#
# 1619. Mean of Array After Removing Some Elements
#
# Q: https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
# A: https://leetcode.com/problems/mean-of-array-after-removing-some-elements/discuss/898684/Kt-Js-Py3-Cpp-Sort-Trim-Average
#

from typing import List

class Solution:
    def trimMean(self, A: List[int]) -> float:
        N = len(A)
        K = N // 20
        return sum(sorted(A)[K:-K]) / (N - 2 * K)
