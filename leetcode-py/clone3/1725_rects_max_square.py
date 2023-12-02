#
# 1725. Number Of Rectangles That Can Form The Largest Square
#
# Q: https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
# A: https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/discuss/1020596/Kt-Js-Py3-Cpp-Best-Max-of-Min(length-width)
#

class Solution:
    def countGoodRectangles(self, A: List[List[int]]) -> int:
        best = max(min(l, w) for l, w in A)
        return len([l for l, w in A if best <= l and best <= w])
