#
# https://leetcode.com/contest/weekly-contest-201/
# https://www.youtube.com/watch?v=cMqzxy8npo0&feature=youtu.be
#
# Rank            Name            Score    Finish Time    Q1 (3)     Q2 (4)    Q3 (6)   Q4 (7)
# 3742 / 10002    claytonjwong    7        1:02:06        0:06:59    1:02:06
#

#
# 1544. Make The String Great
#
# Q: https://leetcode.com/problems/make-the-string-great/
# A: https://leetcode.com/problems/make-the-string-great/discuss/780878/Javascript-Python3-C%2B%2B-solutions
#
class Solution:
    def makeGood(self, t: str) -> str:
        s = []
        for c in t:
            s.append(c)
            while 2 <= len(s) and abs(ord(s[-2]) - ord(s[-1])) == 32:
                s.pop()
                s.pop()
        return ''.join(s)

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
