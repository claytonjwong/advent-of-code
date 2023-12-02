#
# 1564. Put Boxes Into the Warehouse I
#
# Q: https://leetcode.com/problems/put-boxes-into-the-warehouse-i/
# A: https://leetcode.com/problems/put-boxes-into-the-warehouse-i/discuss/817303/Javascript-Python3-C%2B%2B-Greedy
#

from typing import List

class Solution:
    def maxBoxesInWarehouse(self, box: List[int], spot: List[int], cnt = 0) -> int:
		 # 1. preprocess the boxes and spots
        box.sort(reverse=True)
        for j in range(1, len(spot)):
            spot[j] = min(spot[j], spot[j - 1])
		# 2. greedily place i-th min box into j-th min spot (if it fits) from 👈 right-to-left
        i = len(box) - 1
        j = len(spot) - 1
        while 0 <= i and 0 <= j:
            if box[i] <= spot[j]:  # ✅ i-th min box fits in j-th min spot
                i -= 1
                j -= 1
                cnt += 1
            else:                  # 🚫 try next monotonically non-decreasing j-th min spot
                j -= 1
        return cnt
