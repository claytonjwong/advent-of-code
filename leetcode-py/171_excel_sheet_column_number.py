#
# 171. Excel Sheet Column Number
#
# Q: https://leetcode.com/problems/excel-sheet-column-number/
# A: https://leetcode.com/problems/excel-sheet-column-number/discuss/594372/Javascript-Python3-C%2B%2B-1-Liners
#

class Solution:
    def titleToNumber(self, s: str) -> int:
        return reduce(lambda a, b: a + b, [26 ** i * (ord(c) - 64) for i, c in enumerate(reversed([c for c in s]))])
