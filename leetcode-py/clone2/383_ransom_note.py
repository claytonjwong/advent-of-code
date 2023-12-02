#
# 383. Ransom Note
#
# Q: https://leetcode.com/problems/ransom-note/
# A: https://leetcode.com/problems/ransom-note/discuss/611792/Javascript-Python3-C%2B%2B-do-we-have-what-we-need
#

from collections import Counter

class Solution:
    def canConstruct(self, A: str, B: str) -> bool:
        need = Counter(A)
        have = Counter(B)
        return not need - have
