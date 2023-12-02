#
# 344. Reverse String
#
# Q: https://leetcode.com/problems/reverse-string/
# A: https://leetcode.com/problems/reverse-string/discuss/670042/Kt-Js-Py3-Cpp-Easy-or-Hard
#

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

class Solution:
    def reverseString(self, s: List[str]) -> None:
        N = len(s)
        for i in range(N // 2):
            s[i], s[N - 1 - i] = s[N - 1 - i], s[i]
