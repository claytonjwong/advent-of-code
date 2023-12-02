#
# 1710. Maximum Units on a Truck
#
# Q: https://leetcode.com/problems/maximum-units-on-a-truck/
# A: https://leetcode.com/problems/maximum-units-on-a-truck/discuss/999095/Kt-Js-Py3-Cpp-BEST-Greedily-TAKE-BOXES-while-we-HAVE-room
#

from typing import List
from functools import cmp_to_key

class Solution:
    def maximumUnits(self, A: List[List[int]], have: int, best = 0) -> int:
        A.sort(key = cmp_to_key(lambda a, b: b[1] - a[1]))
        for boxes, units in A:
            take = min(have, boxes)
            best += take * units
            have -= take
        return best
