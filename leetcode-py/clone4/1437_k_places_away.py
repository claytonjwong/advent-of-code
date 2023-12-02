#
# 1437. Check If All 1's Are at Least Length K Places Away
#
# Q: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
# A: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/discuss/613577/Kt-Js-Py3-Cpp-Last-Seen-Index
#

class Solution:
    def kLengthApart(self, A: List[int], K: int, last = -1e5) -> bool:
        for i in range(len(A)):
            if not A[i]:
                continue
            ok = K < i - last; last = i
            if not ok:
                return False
        return True
