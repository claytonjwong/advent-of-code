#
# 258. Add Digits
#
# Q: https://leetcode.com/problems/add-digits/
# A: https://leetcode.com/problems/add-digits/discuss/756944/Javascript-Python3-C%2B%2B-1-Liners
#

# using reduce() to accumulate the digits of x
class Solution:
    def addDigits(self, x: int) -> int:
        return x if x < 10 else self.addDigits(reduce(lambda a, b: a + b, map(lambda s: int(s), str(x))))

# using sum() to accumulate the digits of x
class Solution:
    def addDigits(self, x: int) -> int:
        return x if x < 10 else self.addDigits(sum(map(lambda c: int(c), str(x))))
