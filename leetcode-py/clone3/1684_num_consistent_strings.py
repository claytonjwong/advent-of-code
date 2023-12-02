#
# 1684. Count the Number of Consistent Strings
#
# Q: https://leetcode.com/problems/count-the-number-of-consistent-strings/
# A: https://leetcode.com/problems/count-the-number-of-consistent-strings/discuss/969513/Kt-Js-Py3-Cpp-1-Liners
#

from typing import List

# 1-liner
class Solution:
    def countConsistentStrings(self, A: str, words: List[str]) -> int:
        return sum([all([c in set(A) for c in word]) for word in words])

# verbose
class Solution:
    def countConsistentStrings(self, A: str, words: List[str], cnt = 0) -> int:
        dict = set(A)
        for word in words:
            if all([c in dict for c in word]):
                cnt += 1
        return cnt
