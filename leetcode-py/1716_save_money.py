#
# 1716. Calculate Money in Leetcode Bank
#
# Q: https://leetcode.com/problems/calculate-money-in-leetcode-bank/
# A: https://leetcode.com/problems/calculate-money-in-leetcode-bank/discuss/1008853/Kt-Js-Py3-Cpp-Iterative-Accumulation
#

class Solution:
    def totalMoney(self, n: int, start = 1, x = 0, total = 0) -> int:
        for day in range(n):
            if day % 7 == 0:
                x = start; start += 1
            total += x; x += 1
        return total
