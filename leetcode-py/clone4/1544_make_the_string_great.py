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
