#
# 484. Find Permutation
#
# Q: https://leetcode.com/problems/find-permutation/
# A: https://leetcode.com/problems/find-permutation/discuss/795156/Javascript-Python3-C%2B%2B-.-Greedy-Mountain
#

from typing import List

class Solution:
    def findPermutation(self, t: str) -> List[int]:
        s, ans = [], []
        A = list(t)
        A.append('I')                      # 🛑 sentinel value to exhaust last downslope xor append max value last
        for i in range(len(A)):
            s.append(i + 1)                # +1 for 1-based indexing
            while A[i] == 'I' and len(s):
                ans.append(s.pop())        # 💥 greedily consume current upslope xor exhaust pending downslope
        return ans
