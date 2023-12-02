#
# 1672. Richest Customer Wealth
#
# Q: https://leetcode.com/problems/richest-customer-wealth/
# A: https://leetcode.com/problems/richest-customer-wealth/discuss/952772/Kt-Js-Py3-Cpp-1-Liners
#

from typing import List

class Solution:
    def maximumWealth(self, A: List[List[int]]) -> int:
        return max(sum(row) for row in A)
