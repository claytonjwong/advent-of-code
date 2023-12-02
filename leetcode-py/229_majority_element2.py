#
# 229. Majority Element II
#
# Q: https://leetcode.com/problems/majority-element-ii/
# A: https://leetcode.com/problems/majority-element-ii/discuss/859901/Javascript-Python3-C%2B%2B-Naive-solutions
#

from typing import List

class Solution:
    def majorityElement(self, A: List[int]) -> List[int]:
        return [x for x, cnt in Counter(A).most_common(2) if len(A) / 3 < cnt]
