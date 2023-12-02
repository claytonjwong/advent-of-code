#
# 290. Word Pattern
#
# Q: https://leetcode.com/problems/word-pattern/
# A: https://leetcode.com/problems/word-pattern/discuss/622795/Javascript-Python3-C%2B%2B-.-Map-solutions
#

class Solution:
    def wordPattern(self, A: str, B: str) -> bool:
        chars, words = list(A), B.split(' ')
        if len(chars) != len(words):
            return False
        N = len(chars)
        P, T = {}, {}                              # 🗺 pattern, text
        for i in range(N):
            c, w = chars[i], words[i]
            if c in P and P[c] != w: return False  # 🚫 char c not mapped to word w
            if w in T and T[w] != c: return False  # 🚫 word w not mapped to char c
            if c not in P: P[c] = w                # map char c 👉 word w
            if w not in T: T[w] = c                # map word w 👉 char c
        return True  # ✅ OK
