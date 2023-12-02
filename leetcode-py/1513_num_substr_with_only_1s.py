#
# 1513. Number of Substrings With Only 1s
#
# Q: https://leetcode.com/problems/number-of-substrings-with-only-1s/
# A: https://leetcode.com/problems/number-of-substrings-with-only-1s/discuss/731600/Javascript-Python3-C%2B%2B
#

class Solution:
    def numSub(self, s: str) -> int:
        return reduce(lambda sum, n: (sum + (n * (n + 1)) // 2) % int(1e9 + 7), list(map(lambda run: len(run), s.split('0'))), 0)
