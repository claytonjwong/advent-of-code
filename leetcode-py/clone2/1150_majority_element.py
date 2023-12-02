#
# 1150. Check If a Number Is Majority Element in a Sorted Array
#
# Q: https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/
# A: https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/discuss/854521/Javascript-Python3-C%2B%2B-Equal-Range-via-.-Binary-Search
#

from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def isMajorityElement(self, A: List[int], T: int) -> bool:
        i, j = bisect_left(A, T), bisect_right(A, T)
        return len(A) // 2 < j - i
