#
# 161. One Edit Distance
#
# Q: https://leetcode.com/problems/one-edit-distance/
# A: https://leetcode.com/problems/one-edit-distance/discuss/152967/Kt-Js-Py3-Cpp-Linear-Scan
#

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        M = len(s)
        N = len(t)
        i = 0
        j = 0
        k = 0
        while abs(i - j) <= 1 and not (M <= i and N <= j):
            if i < M and j < N and s[i] == t[j]:
                i += 1
                j += 1
            else:
                k += 1
                i = i + 1 if N <= M else i
                j = j + 1 if M <= N else j
        return k == 1
