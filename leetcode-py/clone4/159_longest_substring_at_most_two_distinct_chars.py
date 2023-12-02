#
# 159. Longest Substring with At Most Two Distinct Characters
#
# Q: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
# A: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/discuss/854873/Kt-Js-Py3-Cpp-Sliding-Window-%2B-Map
#

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str, best = 0) -> int:
        m = {}
        N = len(s)
        i = 0
        j = 0
        while j < N:
            m[s[j]] = m[s[j]] + 1 if s[j] in m else 1; j += 1  # ✅ expand window with s[j]
            while 2 < len(m):                                  # ❌ shrink window with s[i] until there are at most 2 distinct chars
                m[s[i]] -= 1
                if not m[s[i]]:
                    del m[s[i]]
                i += 1
            best = max(best, j - i)                            # 🎯 longest substring with at most 2 distinct chars
        return best
