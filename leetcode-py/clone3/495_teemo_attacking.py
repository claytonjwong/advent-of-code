#
# 495. Teemo Attacking
#
# Q: https://leetcode.com/problems/teemo-attacking/
# A: https://leetcode.com/problems/teemo-attacking/discuss/865500/Javascript-Python3-C%2B%2B-Accumulate-Non-overlapping-Intervals-i..j
#

from typing import List

# concise
class Solution:
    def findPoisonedDuration(self, A: List[int], K: int, hi = -1, total = 0) -> int:
        for x in A:
            i = max(hi, x)
            j = x + K
            total += j - i
            hi = max(hi, j)
        return total

# verbose
class Solution:
    def findPoisonedDuration(self, A: List[int], K: int, hi = -1, total = 0) -> int:
        for x in A:
            i = max(hi, x)
            j = x + K - 1            # -1 for i..j inclusive
            total += j - i + 1       # +1 for i..j inclusive
            hi = max(hi, j + 1)      # +1 to skip past redundant timeslot j
        return total
