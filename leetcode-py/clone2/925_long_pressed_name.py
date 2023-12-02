#
# 925. Long Pressed Name
#
# Q: https://leetcode.com/problems/long-pressed-name/
# A: https://leetcode.com/problems/long-pressed-name/discuss/659364/Javascript-Python3-C%2B%2B-Count
#

class Solution:
    def isLongPressedName(self, A: str, B: str) -> bool:
        M = len(A)
        N = len(B)
        i = 0
        j = 0
        while i < M and j < N:
            cntA = 0
            cntB = 0
            while i + 1 < M and A[i] == A[i + 1]: i += 1; cntA += 1
            while j + 1 < N and B[j] == B[j + 1]: j += 1; cntB += 1
            if A[i] != B[j] or cntA > cntB:
                return False
            i += 1
            j += 1
        return i == M and j == N
