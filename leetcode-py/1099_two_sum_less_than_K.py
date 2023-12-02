#
# 1099. Two Sum Less Than K
#
# Q: https://leetcode.com/problems/two-sum-less-than-k/
# A: https://leetcode.com/problems/two-sum-less-than-k/discuss/603797/Kt-Js-Py3-Cpp-Greedy-%2B-Brute-Force-solutions
#

from typing import List

# greedy
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int, best = -1) -> int:
        A.sort()
        N = len(A)
        i = 0
        j = N - 1
        while i < j:
            if A[i] + A[j] < K:
                best = max(best, A[i] + A[j])
                i += 1
            else:
                j -= 1
        return best

# brute-force
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int, best = -1) -> int:
        N = len(A)
        for i in range(N):
            for j in range(i + 1, N):
                if A[i] + A[j] < K:
                    best = max(best, A[i] + A[j])
        return best
