#
# 340. Longest Substring with At Most K Distinct Characters
#
# Q: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# A: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/discuss/992358/Kt-Js-Py3-Cpp-Sliding-Window-%2B-Map
#

from collections import Counter

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int, best = 0) -> int:
        m = Counter()
        i = 0
        j = 0
        N = len(s)
        while j < N:
            m[s[j]] += 1; j += 1
            while k < len(m):        # ⭐️ maintain invariant
                m[s[i]] -= 1
                if not m[s[i]]:
                    del m[s[i]]
                i += 1
            best = max(best, j - i)  # 🎯 maximum length window
        return best
