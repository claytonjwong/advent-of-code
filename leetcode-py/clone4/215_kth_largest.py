#
# 215. Kth Largest Element in an Array
#
# Q: https://leetcode.com/problems/kth-largest-element-in-an-array/
# A: https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/153981/Kt-Js-Py3-Cpp-Sort
#

class Solution:
    def findKthLargest(self, A: List[int], K: int) -> int:
        N = len(A)
        A.sort()
        return A[N - K]
