#
# 1342. Number of Steps to Reduce a Number to Zero
#
# Q: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# A: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/discuss/504160/Javascript-Python3-C%2B%2B-1-Liners
#

class Solution:
    def numberOfSteps (self, x: int) -> int:
        return 0 if not x else 1 + self.numberOfSteps(x - 1 if x % 2 else x // 2)
