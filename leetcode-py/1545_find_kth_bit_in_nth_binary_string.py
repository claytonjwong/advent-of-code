#
# 1545. Find Kth Bit in Nth Binary String
#
# Q: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
# A: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/discuss/780890/Javascript-Python3-C%2B%2B-solutions
#
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def go(i):
            if not i:
                return ['0']
            pre = go(i - 1)
            return pre + ['1'] + list(map(lambda c: '1' if c == '0' else '0', pre))[::-1]
        return go(n - 1)[k - 1]
