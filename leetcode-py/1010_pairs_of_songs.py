#
# 1010. Pairs of Songs With Total Durations Divisible by 60
#
# Q: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# A: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/256716/Kt-Js-Py3-Cpp-Map-of-Buckets
#

from typing import List

class Solution:
    def numPairsDivisibleBy60(self, A: List[int], pairs = 0) -> int:
        m = {}
        A = [x % 60 for x in A]
        for x in A:
            y = (60 - x) % 60
            pairs += m[y] if y in m else 0
            m[x] = 1 + m[x] if x in m else 1
        return pairs
