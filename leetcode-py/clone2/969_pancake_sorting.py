#
# 969. Pancake Sorting
#
# Q: https://leetcode.com/problems/pancake-sorting/
# A: https://leetcode.com/problems/pancake-sorting/discuss/818425/Javascript-Python3-C%2B%2B-Insertion-Sort
#

from typing import List

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        flip = []
        N = len(A)
        for i in range(N - 1, -1, -1):
            if A[i] == i + 1:  # ✅ i-th max value already in i-th position
                continue
            j = A.index(i + 1)
            flip.append(j + 1); A[0:j + 1] = A[0:j + 1][::-1]  # 1. move i-th max value to front
            flip.append(i + 1); A[0:i + 1] = A[0:i + 1][::-1]  # 2. move i-th max value to i-th position
        return flip
