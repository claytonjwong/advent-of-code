#
# 724. Find Pivot Index
#
# Q: https://leetcode.com/problems/find-pivot-index/
# A: https://leetcode.com/problems/find-pivot-index/discuss/751936/Javascript-Python3-C%2B%2B-Prefix-Sums
#

class Solution:
    def pivotIndex(self, A: List[int]) -> int:
        N = len(A)
        L = [0] * N
        R = [0] * N
        beg = 1
        end = N - 2
        for i in range(beg, N):      L[i] = L[i - 1] + A[i - 1] # non-inclusive prefix sums from Left-to-right 👉
        for j in range(end, -1, -1): R[j] = R[j + 1] + A[j + 1] # non-inclusive suffix sums from Right-to-left 👈
        for k in range(N):
            print(k, L[k], R[k])
            if L[k] == R[k]:
                return k # 🎯 target at k-th index
        return -1
