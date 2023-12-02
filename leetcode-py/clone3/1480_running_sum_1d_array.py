#
# 1480. Running Sum of 1d Array
#
# Q: https://leetcode.com/problems/running-sum-of-1d-array/
# A: https://leetcode.com/problems/running-sum-of-1d-array/discuss/686233/Javascript-and-C%2B%2B-solutions
#

class Solution:
    def runningSum(self, A: List[int], sum = 0) -> List[int]:
        N = len(A)
        for i in range (1, N):
            A[i] += A[i - 1]
        return A
