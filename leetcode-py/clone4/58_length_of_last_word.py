#
# 58. Length of Last Word
#
# Q: https://leetcode.com/problems/length-of-last-word/
# A: https://leetcode.com/problems/length-of-last-word/discuss/847943/Javascript-Python3-C%2B%2B-Simple-solutions
#

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        A = [s for s in s.split() if len(s)]
        return len(A[-1]) if len(A) else 0
