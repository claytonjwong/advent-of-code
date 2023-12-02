#
# 179. Largest Number
#
# Q: https://leetcode.com/problems/largest-number/
# A: https://leetcode.com/problems/largest-number/discuss/864389/Javascript-Python3-C%2B%2B-Concise-solutions
#

from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, A: List[int]) -> str:
        S = [str(x) for x in A]
        S.sort(key = cmp_to_key(lambda a, b: 1 if a + b < b + a else -1))
        return '0' if all([c == '0' for c in S]) else ''.join(S)
