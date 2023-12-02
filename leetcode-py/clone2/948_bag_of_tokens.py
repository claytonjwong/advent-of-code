#
# 948. Bag of Tokens
#
# Q: https://leetcode.com/problems/bag-of-tokens/
# A: https://leetcode.com/problems/bag-of-tokens/discuss/909784/Kt-Js-Py3-Cpp-Greedy-Max-Score
#

from typing import List

class Solution:
    def bagOfTokensScore(self, A: List[int], power: int, score = 0, best = 0) -> int:
        A.sort()
        N = len(A)
        i = 0
        j = N - 1
        while i <= j and (A[i] <= power or 0 < score):
            if A[i] <= power:
                power -= A[i]; score += 1; i += 1
            elif 0 < score:
                power += A[j]; score -= 1; j -= 1
            best = max(best, score)
        return best
