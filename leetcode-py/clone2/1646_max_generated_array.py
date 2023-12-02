#
# 1646. Get Maximum in Generated Array
#
# Q: https://leetcode.com/problems/get-maximum-in-generated-array/
# A: https://leetcode.com/problems/get-maximum-in-generated-array/discuss/927494/Kt-Js-Py3-Cpp-Max-of-Generated-Array
#

class Solution:
    def getMaximumGenerated(self, N: int) -> int:
        if N < 2:
            return N
        A = [0] * (N + 1)
        A[0] = 0
        A[1] = 1
        i = 1
        while 2 * i <= N:
            if 2 * i     <= N: A[2 * i    ] = A[i]
            if 2 * i + 1 <= N: A[2 * i + 1] = A[i] + A[i + 1]
            i += 1
        return max(A)
