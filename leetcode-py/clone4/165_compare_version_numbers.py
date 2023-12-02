#
# 165. Compare Version Numbers
#
# Q: https://leetcode.com/problems/compare-version-numbers/
# A: https://leetcode.com/problems/compare-version-numbers/discuss/838238/Javascript-Python3-C%2B%2B-solutions
#

class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        A = [int(s) for s in v1.split('.')]
        B = [int(s) for s in v2.split('.')]
        while len(A) < len(B): A.append(0)
        while len(B) < len(A): B.append(0)
        for i in range(len(A)):
            if A[i] < B[i]: return -1
            if B[i] < A[i]: return  1
        return 0
