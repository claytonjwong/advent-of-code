#
# 1551. Minimum Operations to Make Array Equal
#
# Q: https://leetcode.com/problems/minimum-operations-to-make-array-equal/discuss/794101/Javascript-Python3-C%2B%2B-Single-xor-Double-Middle
# A: https://leetcode.com/problems/minimum-operations-to-make-array-equal/discuss/794101/Javascript-Python3-C%2B%2B-Single-xor-Double-Middle
#

# concise
class Solution:
    def minOperations(self, n: int, ans = 0) -> int:
        return floor(n / 2) * floor((n + 1) / 2)

# verbose
class Solution:
    def minOperations(self, n: int, ans = 0) -> int:
        cur = 2 if n % 2 else 1
        for i in range(floor(n / 2)):
            ans += cur
            cur += 2
        return ans
