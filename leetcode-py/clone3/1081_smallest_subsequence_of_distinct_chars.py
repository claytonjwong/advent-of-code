#
# 1081. Smallest Subsequence of Distinct Characters
#
# Q: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# A: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/discuss/891644/Kt-Js-Py3-C%2B%2B-Monotonic-Queue-%2B-Detailed-Explanation
#

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        A, have = [], set()
        last = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            while c not in have and len(A) and ord(c) < ord(A[-1]) and i < last[A[-1]]:
                have.remove(A.pop())
            if c not in have:
                have.add(c); A.append(c)
        return ''.join(A)
