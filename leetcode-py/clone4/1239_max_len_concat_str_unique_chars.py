#
# 1239. Maximum Length of a Concatenated String with Unique Characters
#
# Q: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
# A: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/discuss/786020/Javascript-Python3-C%2B%2B-hash-collisions
#

from typing import List

class Solution:
    def maxLength(self, A: List[str]) -> int:
        A = list(filter(lambda s: len(set(s)) == len(s), A)) # ❌ remove invalid s
        def go(i = 0, pre = 0):
            if i == len(A):
                return 0
            cur = reduce(lambda hash, c: hash | 1 << (ord(c) - ord('a')), list(A[i]), 0)
            if pre & cur != 0:
                 return go(i + 1, pre) # 💥 collision of non-unique chars, thus we only consider 🚫 without A[i]
            else:
                return max(go(i + 1, pre), len(A[i]) + go(i + 1, pre | cur)) # max of 🚫 without A[i] xor ✅ with A[i]
        return go()
