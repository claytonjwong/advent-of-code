#
# 520. Detect Capital
#
# Q: https://leetcode.com/problems/detect-capital/
# A: https://leetcode.com/problems/detect-capital/discuss/766995/Javascript-Python3-C%2B%2B-1-Liners-%2B-Lambdas
#

# 1-Liner
class Solution:
    def detectCapitalUse(self, s: str) -> bool:
        return all(97 <= ord(c) for c in s) or all(ord(c) <= 90 for c in s) or (ord(s[0]) <= 90 and all(97 <= ord(c) for c in s[1:]))

# 3-Liner
class Solution:
    def detectCapitalUse(self, s: str) -> bool:
        lower = lambda s: all(97 <= ord(c) for c in s)
        upper = lambda s: all(ord(c) <= 90 for c in s)
        return lower(s) or upper(s) or (upper(s[0]) and lower(s[1:]))
