#
# 1550. Three Consecutive Odds
#
# Q: https://leetcode.com/problems/three-consecutive-odds/
# A: https://leetcode.com/problems/three-consecutive-odds/discuss/794079/Javascript-Python3-C%2B%2B-1-Liners-via-reduce()
#

class Solution:
    def threeConsecutiveOdds(self, A: List[int]) -> bool:
        return reduce(lambda found, i: found if i < 2 else found or ((A[i - 2] % 2) and (A[i - 1] % 2) and (A[i] % 2)), [i for i in range(len(A))], False)
