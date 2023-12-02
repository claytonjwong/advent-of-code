#
# 217. Contains Duplicate
#
# Q: https://leetcode.com/problems/contains-duplicate/
# A: https://leetcode.com/problems/contains-duplicate/discuss/824996/Javascript-Python3-C%2B%2B-1-Liners-Seen-Set
#

from typing import List

class Solution:
    def containsDuplicate(self, A: List[int]) -> bool:
        return len(A) != len(set(A))

class Solution:
    def containsDuplicate(self, A: List[int]) -> bool:
        S = set()
        for x in A:
            if x in S:
                return True
            S.add(x)
        return False
