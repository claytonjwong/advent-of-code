#
# 1486. XOR Operation in an Array
#
# Q: https://leetcode.com/problems/xor-operation-in-an-array/
# A: https://leetcode.com/problems/xor-operation-in-an-array/discuss/700800/Javascript-and-C%2B%2B-solutions
#

# recursive
class Solution:
    def xorOperation(self, n: int, x: int) -> int:
        return x if n == 1 else x ^ self.xorOperation(n - 1, x + 2)

# iterative
class Solution:
    def xorOperation(self, n: int, x: int) -> int:
        return reduce(lambda a, b: a ^ b, (map(lambda i: x + 2 * i, [i for i in range(n)])), 0)
