#
# 1680. Concatenation of Consecutive Binary Numbers
#
# Q: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
# A: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/discuss/962337/Kt-Js-Py3-Cpp-Construct-and-sum-Accumulate
#

from math import log2

class Solution:
    def concatenatedBinary(self, N: int, k = 1, mod = int(1e9 + 7), ans = 0) -> int:
        s = []
        for x in range(1, N + 1):
            pad = False
            for i in range(int(log2(x)), -1, -1):
                if x & (1 << i):
                    s.append('1'); pad = True
                elif pad:
                    s.append('0')
        for c in reversed(s):
            if c == '1':
                ans = (ans + k) % mod
            k = 2 * k % mod
        return ans
