#
# 532. K-Diff Pairs in Array
#
# Q: https://leetcode.com/problems/k-diff-pairs-in-an-array/
# A: https://leetcode.com/problems/k-diff-pairs-in-an-array/discuss/596830/Javascript-Python3-C%2B%2B-Concise-solutions
#

from typing import List

class Solution:
    def findPairs(self, A: List[int], K: int) -> int:
        seen, pairs = set(), set()
        pair = lambda a, b: pairs.add(f'{a},{b}' if a < b else f'{b},{a}')
        for x in A:
            if x + K in seen: pair(x, x + K)
            if x - K in seen: pair(x, x - K)
            seen.add(x)
        return len(pairs)
