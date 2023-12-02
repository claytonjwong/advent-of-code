#
# 120. Triangle
#
# Q: https://leetcode.com/problems/triangle/
# A: https://leetcode.com/problems/triangle/discuss/38726/Kt-Js-Py3-Cpp-The-ART-of-Dynamic-Programming
#

# TopDown
class Solution:
    def minimumTotal(self, A: List[List[int]]) -> int:
        N = len(A)
        def go(i = 0, j = 0):
            if i == N:
                return 0
            return A[i][j] + min(go(i + 1, j), go(i + 1, j + 1))
        return go()

# TopDownMemo
class Solution:
    def minimumTotal(self, A: List[List[int]]) -> int:
        N = len(A)
        @cache
        def go(i = 0, j = 0):
            if i == N:
                return 0
            return A[i][j] + min(go(i + 1, j), go(i + 1, j + 1))
        return go()

# BottomUp
class Solution:
    def minimumTotal(self, A: List[List[int]]) -> int:
        N = len(A)
        for i in range(N - 2, -1, -1):
            for j in range(0, len(A[i])):
                A[i][j] += min(A[i + 1][j], A[i + 1][j + 1])
        return A[0][0]
