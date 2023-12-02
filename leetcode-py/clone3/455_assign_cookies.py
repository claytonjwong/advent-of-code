#
# 455. Assign Cookies
#
# Q: https://leetcode.com/problems/assign-cookies/
# A: https://leetcode.com/problems/assign-cookies/discuss/93990/Javascript-Python3-C%2B%2B-Greedy
#

from typing import List

# concise
class Solution:
    def findContentChildren(self, need: List[int], have: List[int], i = 0, j = 0) -> int:
        need.sort()
        have.sort()
        while i < len(need) and j < len(have):
            if need[i] <= have[j]:
                i += 1
            j += 1
        return i

# verbose
class Solution:
    def findContentChildren(self, need: List[int], have: List[int], cnt = 0) -> int:
        need.sort()
        have.sort()
        j = 0
        for i in range(len(need)):
            while j < len(have) and not (need[i] <= have[j]):
                j += 1
            if j < len(have) and need[i] <= have[j]:
                cnt += 1
                j += 1
        return cnt
