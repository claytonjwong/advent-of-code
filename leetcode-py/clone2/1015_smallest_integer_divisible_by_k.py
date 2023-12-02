#
# 1015. Smallest Integer Divisible by K
#
# Q: https://leetcode.com/problems/smallest-integer-divisible-by-k/
# A: https://leetcode.com/problems/smallest-integer-divisible-by-k/discuss/261255/Kt-Js-Py3-Cpp-Mod-K
#

class Solution:
    def smallestRepunitDivByK(self, K: int, i = 1, N = 1) -> int:
        seen = set()
        while True:
            mod = N % K
            if not mod:
                return i
            if mod in seen:
                break
            seen.add(mod)
            N = (10 * N + 1) % K
            i += 1
        return -1
