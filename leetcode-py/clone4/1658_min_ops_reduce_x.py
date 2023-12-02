#
# 1658. Minimum Operations to Reduce X to Zero
#
# Q: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# A: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/1016764/Kt-Js-Py3-Cpp-Sliding-Window
#

class Solution:
    def minOperations(self, A: List[int], K: int, best = 0) -> int:
        T = sum(A) - K
        N = len(A)
        if not T:                            # 💎 corner case: if sum(A) == K, then minimum is N
            return N
        i = 0
        j = 0
        t = 0
        while j < N:
            while i < j and T < t + A[j]:    # ⭐️ maintain invariant: sliding window total t does NOT exceed target T
                t -= A[i]; i += 1
            t += A[j]; j += 1
            if t == T:
                best = max(best, j - i)      # 💰 best "middle" subarray length [i..j), ie. from i inclusive to j non-inclusive
        return -1 if not best else N - best  # 🎯 minimum "left/right" subarray length == N - best
