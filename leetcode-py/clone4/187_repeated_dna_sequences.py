#
# 187. Repeated DNA Sequences
#
# Q: https://leetcode.com/problems/repeated-dna-sequences/
# A: https://leetcode.com/problems/repeated-dna-sequences/discuss/898609/Kt-Js-Py3-Cpp-Sliding-Window-%2B-Map
#

from typing import List
from collections import deque

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        m = {}
        word = deque()
        for c in s:
            if len(word) == 10:
                word.popleft()
            word.append(c)
            key = ''.join(word)
            m[key] = m[key] + 1 if key in m else 1
        return [word for word, cnt in m.items() if 1 < cnt]
