#
# 1492. The kth Factor of n
#
# Q: https://leetcode.com/problems/the-kth-factor-of-n/
# A: https://leetcode.com/problems/the-kth-factor-of-n/discuss/708074/Kt-Js-Py3-Cpp-solution
#

class Solution:
    def kthFactor(self, N: int, K: int) -> int:
        for i in range(1, N + 1):
            if not (N % i):
                K -= 1
                if not K:
                    return i
        return -1
