#
# 389. Find the Difference
#
# Q: https://leetcode.com/problems/find-the-difference/
# A: https://leetcode.com/problems/find-the-difference/discuss/862287/Javascript-Python3-C%2B%2B-Concise-solutions
#

from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum([ord(c) for c in t]) - sum([ord(c) for c in s]))

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return [key for key in (Counter(t) - Counter(s))][0]
