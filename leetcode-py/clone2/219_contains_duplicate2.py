#
# 219. Contains Duplicate II
#
# Q: https://leetcode.com/problems/contains-duplicate-ii/
# A: https://leetcode.com/problems/contains-duplicate-ii/discuss/825078/Javascript-Python3-C%2B%2B-Sliding-Window-Seen-Set
#

from typing import List

class Solution:
    def containsNearbyDuplicate(self, A: List[int], K: int) -> bool:
        S = set()
        for i in range(0, len(A)):
            if A[i] in S:           # 🎯 duplicate in window
                return True
            S.add(A[i])             # ✅ add value in window
            if 0 <= i - K:
                S.remove(A[i - K])  # 🚫 delete value which "fell off the end" as the window slides 👉
        return False
