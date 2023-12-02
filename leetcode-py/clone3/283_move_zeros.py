#
# 283. Move Zeroes
#
# Q: https://leetcode.com/problems/move-zeroes/
# A: https://leetcode.com/problems/move-zeroes/discuss/563206/Javascript-Python3-C%2B%2B-readwrite-index
#

class Solution:
    def moveZeroes(self, A: List[int]) -> None:
        N = len(A)
        i = 0
        j = 0
        while j < N:
            if A[j]:
                A[i] = A[j] # ✅ write each non-zero j-th value, ie. 🚫 skip each zero j-th value 🎱
                i += 1
            j += 1
        while i < N:
            A[i] = 0 # write each 🚫 skipped zero j-th value 🎱 at the end
            i += 1
