#
# 1641. Count Sorted Vowel Strings
#
# Q: https://leetcode.com/problems/count-sorted-vowel-strings/
# A: https://leetcode.com/problems/count-sorted-vowel-strings/discuss/919428/Kt-Js-Py3-Cpp-1-Liners
#

# 1-liners
class Solution:
    def countVowelStrings(self, N: int, last = '0', total = 0) -> int:
        return 1 if not N else sum([self.countVowelStrings(N - 1, c) for c in 'aeiou' if last <= c])

# verbose
class Solution:
    def countVowelStrings(self, N: int, last = '0', total = 0) -> int:
        if not N:
            return 1
        for c in 'aeiou':
            if last <= c:
                total += self.countVowelStrings(N - 1, c)
        return total
