#
# 151. Reverse Words in a String
#
# Q: https://leetcode.com/problems/reverse-words-in-a-string/
# A: https://leetcode.com/problems/reverse-words-in-a-string/discuss/737631/Javascript-Python3-C%2B%2B
#

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
