#
# 1618. Maximum Font to Fit a Sentence in a Screen
#
# Q: https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/
# A: https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/discuss/904856/Kt-Js-Py3-Cpp-Binary-Search
#

from typing import List

class Solution:
    def maxFont(self, s: str, w: int, h: int, A: List[int], fontInfo : 'FontInfo') -> int:
        height = lambda x: fontInfo.getHeight(x)
        width = lambda x: sum([fontInfo.getWidth(x, c) for c in s])
        ok = lambda x: height(x) <= h and width(x) <= w
        N = len(A)
        i = 0
        j = N - 1
        while i < j:
            k = (i + j) // 2
            if ok(A[k + 1]):
                i = k + 1
            else:
                j = k
        return A[i] if ok(A[i]) else -1
