#
# 252. Meeting Rooms
#
# Q: https://leetcode.com/problems/meeting-rooms/
# A: https://leetcode.com/problems/meeting-rooms/discuss/919342/Kt-Js-Py3-Cpp-Sort-%2B-Scan
#

from typing import List

class Solution:
    def canAttendMeetings(self, A: List[List[int]], last = 0) -> bool:
        for i, j in sorted(A):
            if not (last <= i):
                return False
            last = j
        return True
