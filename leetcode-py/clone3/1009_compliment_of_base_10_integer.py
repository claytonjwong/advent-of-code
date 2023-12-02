#
# 1009. Complement of Base 10 Integer
#
# Q: https://leetcode.com/problems/complement-of-base-10-integer/
# A: https://leetcode.com/problems/complement-of-base-10-integer/discuss/613061/Javascript-Python3-C%2B%2B
#

# 1-liner
class Solution:
    def bitwiseComplement(self, x: int) -> int:
        return int(''.join(['1' if bit == '0' else '0' for bit in bin(x)[2:]]), 2)

# verbose
class Solution:
    def bitwiseComplement(self, x: int, i = 1) -> int:
        while i < x:
            i <<= 1
        return 1 if not x else ~x & (i - 1)
