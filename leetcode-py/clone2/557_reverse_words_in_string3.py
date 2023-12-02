#
# 557. Reverse Words in a String III
#
# Q: https://leetcode.com/problems/reverse-words-in-a-string-iii/
# A: https://leetcode.com/problems/reverse-words-in-a-string-iii/discuss/759448/Javascript-Python3-C%2B%2B-solutions
#

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split(' '))
