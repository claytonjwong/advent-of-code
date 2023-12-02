#
# 556. Next Greater Element III
#
# Q: https://leetcode.com/problems/next-greater-element-iii/
# A: https://leetcode.com/problems/next-greater-element-iii/discuss/983450/Kt-Js-Py3-Cpp-Brute-Force-Permutations
#

from itertools import permutations

class Solution:
    def nextGreaterElement(self, T: int, best = 1e9 - 1) -> int:
        A = list(str(T))
        P = list(permutations(A))
        print(P)
        cand = int(''.join(P[1]))
        if T < cand < best:
            best = cand
        return best if best < 1e9 - 1 else -1
