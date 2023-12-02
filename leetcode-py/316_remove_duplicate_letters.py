#
# 316. Remove Duplicate Letters
#
# Q: https://leetcode.com/problems/remove-duplicate-letters/
# A: https://leetcode.com/problems/remove-duplicate-letters/discuss/890223/Kt-Js-Py3-C%2B%2B-Monotonic-Queue-%2B-Detailed-Explanation
#

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        N = len(s)
        have, A = set(), []
        last = { c: i for i, c in enumerate(s) }
        for i, c in enumerate(s):
            while c not in have and len(A) and ord(c) < ord(A[-1]) and i < last[A[-1]]:
                have.remove(A[-1]); A.pop()
            if c not in have:
                have.add(c); A.append(c)
        return ''.join(A)
