#
# 253. Meeting Rooms II
#
# Q: https://leetcode.com/problems/meeting-rooms-ii/
# A: https://leetcode.com/problems/meeting-rooms-ii/discuss/895910/Kt-Js-Py3-Cpp-Maximum-Overlap-via-Map
#

from typing import List

class Solution:
    def minMeetingRooms(self, A: List[List[int]], overlap = 0, maximum = 0) -> int:
        m = {}
        for i, j in A:
            m[i] =  1 if i not in m else m[i] + 1
            m[j] = -1 if j not in m else m[j] - 1
        for _, x in sorted(m.items()):
            overlap += x; maximum = max(maximum, overlap)
        return maximum
