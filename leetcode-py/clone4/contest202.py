#
# Rank            Name            Score    Finish Time    Q1 (3)     Q2 (4)    Q3 (5)   Q4 (6)
# 4757 / 14373    claytonjwong    7        0:17:32        0:01:00    0:17:32
#

#
# 1550. Three Consecutive Odds
#
# Q: https://leetcode.com/problems/three-consecutive-odds/
# A: https://leetcode.com/problems/three-consecutive-odds/discuss/794079/Javascript-Python3-C%2B%2B-1-Liners-via-reduce()
#

class Solution:
    def threeConsecutiveOdds(self, A: List[int]) -> bool:
        return reduce(lambda found, i: found if i < 2 else found or ((A[i - 2] % 2) and (A[i - 1] % 2) and (A[i] % 2)), [i for i in range(len(A))], False)


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
