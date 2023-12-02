#
# 1523. Count Odd Numbers in an Interval Range
#
# Q: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
# A: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/discuss/754764/Javscript-Python3-C%2B%2B-1-Liners
#
class Solution:
    def countOdds(self, i: int, j: int) -> int:
        return max(0, (j - i - 1) // 2) + (i % 2) + (j % 2) + (not (i % 2) and not (j % 2)) - (i == j)
