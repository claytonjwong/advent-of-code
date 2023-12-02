#
# 832. Flipping an Image
#
# Q: https://leetcode.com/problems/flipping-an-image/
# A: https://leetcode.com/problems/flipping-an-image/discuss/131721/Kt-Js-Py3-Cpp-1-Liners
#

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[x ^ 1 for x in reversed(row)] for row in A]
