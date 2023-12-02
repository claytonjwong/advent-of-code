#
# 605. Can Place Flowers
#
# Q: https://leetcode.com/problems/can-place-flowers/
# A: https://leetcode.com/problems/can-place-flowers/discuss/103899/Kt-Js-Py3-Cpp-Greedy-Linear-Scan
#

from typing import List

class Solution:
    def canPlaceFlowers(self, A: List[int], K: int) -> bool:
        N = len(A)
        if not K: return True
        if not N: return False
        if N == 1: return not A[0] and K == 1
        def plant(i):
            nonlocal K
            A[i] = 1; K -= 1
        if A[0] + A[1] == 0:
            plant(0)                             # 🌸 👈 left-most position 0
        for i in range(1, N - 1):
            if A[i - 1] + A[i] + A[i + 1] == 0:
                plant(i)                         # 👉 🌸 👈 middle positions 1..N - 2
        if A[N - 2] + A[N - 1] == 0:
            plant(N - 1)                         # 👉 🌸 right-most position N - 1
        return K <= 0
