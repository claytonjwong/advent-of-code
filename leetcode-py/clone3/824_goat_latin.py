#
# 824. Goat Latin
#
# Q: https://leetcode.com/problems/goat-latin/
# A: https://leetcode.com/problems/goat-latin/discuss/128096/3-liner-C%2B%2B
#

class Solution:
    def toGoatLatin(self, words: str, vowels = set([ 'a','e','i','o','u' ])) -> str:
        isVowel = lambda s: s[0].lower() in vowels
        return ' '.join(s + 'ma' + 'a' * (i + 1) for i, s in enumerate([s if isVowel(s) else s[1:] + s[0] for s in split(' ', words)]))
