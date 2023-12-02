#
# 1554. Strings Differ by One Character
#
# Q: https://leetcode.com/problems/strings-differ-by-one-character/
# A: https://leetcode.com/problems/strings-differ-by-one-character/discuss/804559/Javascript-Python3-C%2B%2B-Diff-Collision-Base-123
#

from typing import List

class Solution:
    def differByOne(self, A: List[str], MOD = int(1e13)) -> bool:
        M = len(A)
        N = len(A[0])
        hash = [0] * M
		# 1. generate each i-th rolling hash
        for i in range(M):
            base = 1
            for j in range(N):
                hash[i] = (hash[i] + base * ord(A[i][j])) % MOD
                base = 123 * base % MOD
		# 2. remove each j-th char from each i-th rolling hash to 🔍 find a diff collision 💥
        seen = set()
        for i in range(M):
            base = 1
            for j in range(N):
                diff = (hash[i] - base * ord(A[i][j])) % MOD
                if diff in seen:
                    return True  # 🎯 found a diff collision 💥
                seen.add(diff)
                base = 123 * base % MOD
        return False
