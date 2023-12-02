#
# 3. Longest Substring Without Repeating Characters
#
# Q: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# A: https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/504179/Kt-Js-Py3-Cpp-Best-i-Last-Seen-Duplicate-Index
#

class Solution:
    def lengthOfLongestSubstring(self, s: str, last = -1, best = 0) -> int:
        m = {}
        for i, c in enumerate(s):
            last = max(last, m[c] if c in m else -1); m[c] = i
            best = max(best, i - last)
        return best
