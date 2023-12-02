#
# 56. Merge Intervals
#
# Q: https://leetcode.com/problems/merge-intervals/
# A: https://leetcode.com/problems/merge-intervals/discuss/940348/Kt-Js-Py3-Cpp-Sort-A-%2B-Track-Overlaps-via-Last-End
#

from typing import List
from functools import cmp_to_key

class Solution:
    def merge(self, A: List[List[int]]) -> List[List[int]]:
        A.sort(key = cmp_to_key(lambda a, b: a[1] - b[1] if a[0] == b[0] else a[0] - b[0]))
        ans = [A[0]]
        for [beg, end] in A:
            lastIndex = len(ans) - 1
            lastEnd = ans[lastIndex][1]
            if beg <= lastEnd:
                ans[lastIndex][1] = max(lastEnd, end)  # overlap
            else:
                ans.append([beg, end])                 # no overlap
        return ans
