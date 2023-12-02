#
# 1624. Largest Substring Between Two Equal Characters
#
# Q: https://leetcode.com/problems/largest-substring-between-two-equal-characters/
# A: https://leetcode.com/problems/largest-substring-between-two-equal-characters/discuss/900287/Kt-Js-Py3-Cpp-Map-(concise-%2B-verbose)-solutions
#

# concise
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str, best = -1) -> int:
        m = {c: i for i, c in enumerate(s)}
        return max([m[c] - i - 1 for i, c in enumerate(s)])  # -1 for (i..j) non-inclusive

# verbose
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str, best = -1) -> int:
        m = {}
        for i, c in enumerate(s):
            if c in m:
                best = max(best, i - m[c] - 1)  # -1 for (i..j) non-inclusive
            else:
                m[c] = i
        return best
