#
# 1217. Minimum Cost to Move Chips to The Same Position
#
# Q: https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
# A: https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/discuss/399869/Kt-Js-Py3-Cpp-Minimum-Odd-and-Even
#

from typing import List

# concise
class Solution:
    def minCostToMoveChips(self, A: List[int]) -> int:
        return min(len([x for x in A if x & 1]), len([x for x in A if not x & 1]))

# verbose
class Solution:
    def minCostToMoveChips(self, A: List[int], odd = 0, even = 0) -> int:
        for x in A:
            if x & 1:
                odd += 1
            else:
                even += 1
        return min(odd, even)
