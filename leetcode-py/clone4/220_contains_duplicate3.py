#
# 220. Contains Duplicate III
#
# Q: https://leetcode.com/problems/contains-duplicate-iii/
# A: https://leetcode.com/problems/contains-duplicate-iii/discuss/825714/Javascript-Python3-C%2B%2B-Sliding-Window-with-Buckets
#

from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, A: List[int], K: int, T: int) -> bool:
        m = {}
        N = len(A)
        if N < 2:
            return False
        bucket = lambda x: x // T if T else x // (T + 1)  # ⭐️ +1 to avoid division by 0 when T == 0
        ok = lambda i, j: j in m and abs(m[j] - A[i]) <= T
        for i in range(N):
			#  1. check each j-th bucket for case 1 || case 2 || case 3
            j = bucket(A[i])
            if ok(i, j - 1) or ok(i, j) or ok(i, j + 1):  # (👈 adjacent bucket to-the-left || 🎯 same bucket || adjacent bucket to-the-right 👉)
                return True
            # slide window 👉
            m[j] = A[i]                 # ✅ add current value A[i] onto the window by mapping A[i] to the j-th bucket
            if 0 <= i - K:
                end = bucket(A[i - K])  # 🚫 remove end value A[i - K] from window by removing mapping A[i - K] to end-th bucket which "fell off the end" of window of size K
                del m[end]
        return False
