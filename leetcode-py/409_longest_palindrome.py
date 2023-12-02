#
# 409. Longest Palindrome
#
# Q: https://leetcode.com/problems/longest-palindrome/
# A: https://leetcode.com/problems/longest-palindrome/discuss/791485/Javascript-Python3-C%2B%2B-even-count-odd-count-%2B-1
#

class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = collections.Counter(s)
        odd = sum([cnt % 2 for _, cnt in m.items()])
        return len(s) - odd + (1 if odd else 0)
