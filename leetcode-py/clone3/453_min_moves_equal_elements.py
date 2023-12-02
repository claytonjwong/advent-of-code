#
# 453. Minimum Moves to Equal Array Elements
#
# Q: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# A: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/discuss/492864/Javascript-Python3-C%2B%2B-Min-Element
#

from typing import List

class Solution:
    def minMoves(self, A: List[int]) -> int:
        low = min(A)
        return sum([x - low for x in A])
