#
# 575. Distribute Candies
#
# Q: https://leetcode.com/problems/distribute-candies/
# A: https://leetcode.com/problems/distribute-candies/discuss/668969/Javascript-Python3-C%2B%2B-1-Liners
#

from typing import List

class Solution:
    def distributeCandies(self, A: List[int]) -> int:
        return min(len(set(A)), len(A) // 2)
