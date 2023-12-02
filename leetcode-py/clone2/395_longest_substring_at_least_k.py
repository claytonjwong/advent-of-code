#
# 395. Longest Substring with At Least K Repeating Characters
#
# Q: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
# A: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/949961/Kt-Js-Py3-Cpp-Recursively-Reduce-Search-Space-i..j
#

from collections import Counter

class Solution:
    def longestSubstring(self, s, T, i = 0, j = 1e4, best = 0):
        j = min(j, len(s))
        m = Counter(s[i:j])
        need = {c for c in s[i:j] if m[c] < T}
        if not need:                   # 🎯 valid substring [i..j)
            return j - i
        next = [i - 1]                 # ⭐️ -1 since invalid indexes are non-inclusive (but i is inclusive)
        for k in range(i, j):
            if s[k] in need:
                next.append(k)
        next.append(j)
        for k in range(1, len(next)):  # 🚀 recursively search for valid substrings in between next indexes (previous + 1 because next indexes are non-inclusive)
            best = max(best, self.longestSubstring(s, T, next[k - 1] + 1, next[k]))
        return best
