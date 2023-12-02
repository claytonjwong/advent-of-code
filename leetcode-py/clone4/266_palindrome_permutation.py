#
# 266. Palindrome Permutation
#
# Q: https://leetcode.com/problems/palindrome-permutation/
# A: https://leetcode.com/problems/palindrome-permutation/discuss/592736/Kt-Js-Py3-Cpp-Seen-Odd
#

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        seen = set()
        [seen.remove(c) if c in seen else seen.add(c) for c in s]
        return len(seen) <= 1
