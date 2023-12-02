#
# 88. Merge Sorted Array
#
# Q: https://leetcode.com/problems/merge-sorted-array/
# A: https://leetcode.com/problems/merge-sorted-array/discuss/670661/Kt-Js-Py3-Cpp-Merge-from-Right-to-Left
#

class Solution:
    def merge(self, A: List[int], M: int, B: List[int], N: int) -> None:
        i = M - 1
        j = N - 1
        k = M + N - 1
        while 0 <= j:
            if i < 0 or A[i] < B[j]:
                A[k] = B[j]; j -= 1; k -= 1
            else:
                A[k] = A[i]; i -= 1; k -= 1
