#
# 1558. Minimum Numbers of Function Calls to Make Target Array
#
# Q: https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/
# A: https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/discuss/813579/Javascript-Python3-C%2B%2B-Operation-0-%2B-1
#

from typing import List

class Solution:
    def minOperations(self, A: List[int]) -> int:
        return sum([bin(x).count('1') for x in A]) + math.floor(math.log2(max(A)))
