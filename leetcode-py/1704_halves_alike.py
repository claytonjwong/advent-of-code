#
# 1704. Determine if String Halves Are Alike
#
# Q: https://leetcode.com/problems/determine-if-string-halves-are-alike/
# A: https://leetcode.com/problems/determine-if-string-halves-are-alike/discuss/988139/kt-js-py3-cpp-halves-equal-vowel-count
#

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = set([ 'a', 'e', 'i', 'o', 'u' ])
        N = len(s)
        K = N // 2
        a = s[:K]
        b = s[K:]
        isVowel = lambda c: c.lower() in vowel
        return sum([1 for c in a if isVowel(c)]) == sum(1 for c in b if isVowel(c))
