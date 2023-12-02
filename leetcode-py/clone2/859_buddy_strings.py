#
# 859. Buddy Strings
#
# Q: https://leetcode.com/problems/buddy-strings/
# A: https://leetcode.com/problems/buddy-strings/discuss/141769/Kt-Js-Py3-C%2B%2B-solutions
#

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        M, N = len(A), len(B)
        if M != N or N < 2:
            return False
        if A == B:
            return len(set(A)) < N
        j = -1
        k = -1
        for i in range(N):
            if A[i] != B[i]:
                j = k; k = i
        if j == -1 or k == -1:
            return False
        A = list(A)
        B = list(B)
        A[j], A[k] = A[k], A[j]
        return A == B
