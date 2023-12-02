#
# 119. Pascal's Triangle II
#
# Q: https://leetcode.com/problems/pascals-triangle-ii/
# A: https://leetcode.com/problems/pascals-triangle-ii/discuss/787820/Javascript-Python3-C%2B%2B-current-row-via-previous-row
#

from typing import List

class Solution:
    def getRow(self, k: int) -> List[int]:
        cur = [ 1 ]
        while k:
            pre = cur.copy()
            for i in range(1, len(pre)):
                cur[i] = pre[i - 1] + pre[i]
            cur.append(1)
            k -= 1
        return cur
