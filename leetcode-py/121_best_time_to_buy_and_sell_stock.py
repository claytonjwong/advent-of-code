#
# 121. Best Time to Buy and Sell Stock
#
# Q: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# A: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/507318/Javascript-and-C%2B%2B-solutions
#

class Solution:
    def maxProfit(self, A: List[int], lo = float('inf'), hi = 0) -> int:
        for x in A:
            lo = min(lo, x)
            hi = max(hi, x - lo)
        return hi
