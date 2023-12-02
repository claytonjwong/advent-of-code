#
# 1580. Put Boxes Into the Warehouse II
#
# Q: https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/
# A: https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/discuss/840231/Javascript-Python3-C%2B%2B-Greedy-%2B-Shrinking-Window-i-...-j
#

from typing import List

class Solution:
    def maxBoxesInWarehouse(self, box: List[int], spot: List[int], cnt = 0) -> int:
        box.sort(reverse = True)
        i = 0
        j = len(spot) - 1
        k = 0
        while i <= j and k < len(box):
            if box[k] <= max(spot[i], spot[j]):
                cnt += 1
                if spot[i] < spot[j]:
                    j -= 1
                else:
                    i += 1
            k += 1
        return cnt
