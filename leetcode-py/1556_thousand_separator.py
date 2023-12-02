#
# 1556. Thousand Separator
#
# Q: https://leetcode.com/problems/thousand-separator/
# A: https://leetcode.com/problems/thousand-separator/discuss/805674/Javascript-Python3-C%2B%2B-1-Liners
#

class Solution:
    def thousandSeparator(self, n: int) -> str:
        return str(n) if n < 1000 else self.thousandSeparator(n // 1000) + '.' + str(n % 1000).zfill(3)
