#
# 1417. Reformat The String
#
# Q: https://leetcode.com/problems/reformat-the-string/
# A: https://leetcode.com/problems/reformat-the-string/discuss/586472/Javascript-Python3-C%2B%2B-zip()
#

class Solution:
    def reformat(self, s: str) -> str:
        digits = list(filter(lambda c: ord(c) < 97, list(s)))    # 97 is the ordinal value of 'a'
        letters = list(filter(lambda c: 97 <= ord(c), list(s)))
        if 1 < abs(len(digits) - len(letters)):
            return ''
        ans = []
        if len(digits) == len(letters):
            ans = [x for tuple in zip(letters, digits) for x in tuple]
        if len(digits) < len(letters):
            ans = [x for tuple in zip(letters, digits) for x in tuple] + [letters[-1]]
        if len(letters) < len(digits):
            ans = [x for tuple in zip(digits, letters) for x in tuple] + [digits[-1]]
        return ''.join(ans)
