#
# 1758. Minimum Changes To Make Alternating Binary String
#
# Q: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
# A: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/discuss/1064549/Kt-Js-Py3-Cpp-Explore-2-Candidates
#

class Solution:
    def minOperations(self, s: str, a = 0, b = 1, first = 0, second = 0) -> int:
        ordinal = lambda c: ord(c) - ord('0')
        for c in s:
            if a == ordinal(c): first += 1
            if b == ordinal(c): second += 1
            a ^= 1; b ^= 1
        return min(first, second)
