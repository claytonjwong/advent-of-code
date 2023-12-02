#
# 1695. Maximum Erasure Value
#
# Q: https://leetcode.com/problems/maximum-erasure-value/
# A: https://leetcode.com/problems/maximum-erasure-value/discuss/978556/Kt-Js-Py3-Cpp-Sliding-Window-%2B-Seen-Set
#

from typing import List

class Solution:
    def maximumUniqueSubarray(self, A: List[int], total = 0, best = 0) -> int:
        seen = set()
        N = len(A)
        i = 0
        j = 0
        while j < N:
            if A[j] in seen:         # 👉 shrink window to maintain loop invariant A[i..j] 👀 uniquely seen
                total -= A[i]
                seen.remove(A[i])
                i += 1
            else:                    # 👉 expand window
                total += A[j]
                seen.add(A[j])
                j += 1
            best = max(best, total)  # 🎯 best total A[i..j]
        return best
