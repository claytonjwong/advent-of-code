#
# 1518. Water Bottles
#
# Q: https://leetcode.com/problems/water-bottles/
# A: https://leetcode.com/problems/water-bottles/discuss/743230/Javascript-Python3-C%2B%2B-1-Liners
#

# top-down concise
class Solution:
    def numWaterBottles(self, n: int, k: int) -> int:
        return n if n < k else k + self.numWaterBottles(n - k + 1, k)

# top-down verbose
class Solution:
    def numWaterBottles(self, n: int, k: int) -> int:
        # 🛑 base case: drink all n bottles and 🚫 cannot exchange enough empty bottles for another drink
        if n < k:
            return n
        # 🚀 recursive case: drink k bottles at a time and ✅ exchange those k empty bottles for +1 more drink 🍺
        return k + self.numWaterBottles(n - k + 1, k)

# bottom-up
class Solution:
    def numWaterBottles(self, n: int, k: int, d = 0) -> int:
        while k <= n:
            d = d + k     # 🚀 drink k bottles at a time
            n = n - k + 1 # ✅ exchange k empty bottles for +1 more drink 🍺
        return d + n      # 🛑 drink remaining n bottles and 🚫 cannot exchange enough empty bottles for another drink
