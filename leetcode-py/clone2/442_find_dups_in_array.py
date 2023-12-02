# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/

from typing import List

# O(N) mem
class Solution:
    def findDuplicates(self, A: List[int]) -> List[int]:
        ans = []
        seen = set()
        for x in A:
            if x in seen:
                ans.append(x)
            seen.add(x)
        return ans

# O(1) mem by adding N onto the index corresponding to each value in A, only values seen twice exceed 2 * N
class Solution:
    def findDuplicates(self, A: List[int]) -> List[int]:
        N = len(A)
        for i in A:
            while N < i:
                i -= N
            A[i - 1] += N         # -1 for 0-based indexing
        ans = []
        for i in range(N):
            if 2 * N < A[i]:
                ans.append(i + 1) # +1 for 1-based indexing
        return ans
