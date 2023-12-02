#
# 835. Image Overlap
#
# Q: https://leetcode.com/problems/image-overlap/
# A: https://leetcode.com/problems/image-overlap/discuss/133614/Javascript-Python3-C%2B%2B-Brute-Force
#

from typing import List

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        # 🎯  1. create T by padding B with N - 1 zeros
        N = len(A)
        K = N + 2 * (N - 1)
        T = [[0] * K for _ in range(K)]
        offset = N - 1
        for i in range(offset, 2 * offset + 1):
            for j in range(offset, 2 * offset + 1):
                T[i][j] = B[i - offset][j - offset]
        #  🔍  2. find max overlap by comparing A with all offsets in T
        best = 0
        for offset_i in range(0, 2 * offset + 1):
            for offset_j in range(0, 2 * offset + 1):
                overlap = 0
                for i in range(N):
                    for j in range(N):
                        overlap += A[i][j] & T[i + offset_i][j + offset_j]
                best = max(best, overlap)
        return best
