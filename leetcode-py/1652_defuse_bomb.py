#
# 1652. Defuse the Bomb
#
# Q: https://leetcode.com/problems/defuse-the-bomb/
# A: https://leetcode.com/problems/defuse-the-bomb/discuss/935371/Kt-Js-Py3-Cpp-One-Step-at-a-Time
#

from typing import List

class Solution:
    def decrypt(self, A: List[int], K: int) -> List[int]:
        N = len(A)
        if not K:
            return [0] * N
        if K < 0:
            return self.decrypt(A[::-1], -K)[::-1]
        step = lambda i: i + 1 if i + 1 < N else 0
        ans = []
        for i in range(N):
            steps = K
            total = 0
            j = step(i)
            for _ in range(steps): total += A[j]; j = step(j)
            ans.append(total)
        return ans
