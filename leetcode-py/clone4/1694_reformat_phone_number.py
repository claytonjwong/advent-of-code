#
# 1694. Reformat Phone Number
#
# Q: https://leetcode.com/problems/reformat-phone-number/
# A: https://leetcode.com/problems/reformat-phone-number/discuss/978502/kt-js-py3-cpp-recursive-solutions
#

class Solution:
    def reformatNumber(self, s: str) -> str:
        def go(s):
            N = len(s)
            if N <= 3: return s
            if N == 4: return s[:2] + '-' + s[2:]
            return s[:3] + '-' + go(s[3:])
        return go(''.join([c for c in list(s) if c != ' ' and c != '-']))
