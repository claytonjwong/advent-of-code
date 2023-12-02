#
# 1481. Least Number of Unique Integers after K Removals
#
# Q: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
# A: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/discuss/686410/Kt-Js-Py3-Cpp-Greedy-Drop-K-Least-Frequent-via-Map
#

from typing import List
from functools import cmp_to_key
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, A: List[int], K: int) -> int:
        m = Counter(A)
        A.sort(key = cmp_to_key(lambda a, b: a - b if m[a] == m[b] else m[a] - m[b]))
        return len(set(A[K:]))
