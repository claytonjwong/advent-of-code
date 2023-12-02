#
# 482. License Key Formatting
#
# Q: https://leetcode.com/problems/license-key-formatting/
# A: https://leetcode.com/problems/license-key-formatting/discuss/594395/Javascript-Python3-C%2B%2B-solutions
#

from collections import deque

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        ans = []
        A = [c if c.isnumeric() else c.upper() for c in reversed(S) if c != '-']
        for i in range(len(A)):
            if i and not (i % K):
                ans.append('-')
            ans.append(A[i])
        return ''.join(reversed(ans))

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        ans = deque()
        A = [c if c.isnumeric() else c.upper() for c in S if c != '-']
        while len(A):
            take = min(len(A), K)
            word = deque()
            while take:
                word.appendleft(A.pop())
                take -= 1
            ans.appendleft(''.join(word))
        return '-'.join(ans)
