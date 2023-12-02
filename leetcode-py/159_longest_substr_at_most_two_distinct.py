#
# 159. Longest Substring with At Most Two Distinct Characters
#
# Q: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
# A: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/discuss/854873/Javascript-Python3-C%2B%2B-Sliding-Window-%2B-Map
#

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str, best = 0) -> int:
        m = {}
        N = len(s)
        i = 0                                    # 👉 sliding window [i..j) ie. from i inclusive to j non-inclusive  
        j = 0
        while j < N:                             # 💥 exit upon end of input string s
            while 2 < len(m):                    # 👉 shink window and 💥 exit upon reaching ✅ valid window with 🗺 at-most 2 distinct values
                if s[i] in m and m[s[i]] == i:   # 🚫 delete s[i] at 🗺 right-most index i 👀 🤔
                    del m[s[i]]
                i += 1                           # 👉 shrink window [i..j)
            while j < N and len(m) <= 2:         # 👉 expand window and 💥 exit upon end of input string s xor 🗺 addition of 3rd distinct value at index j
                m[s[j]] = j                      # 📝 remember s[j] is marked for 😵 future deletion at 🗺 right-most index j 👀 🤔
                j += len(m) <= 2                 # 👉 expand window [i..j) while ✅ valid window with 🗺 at-most 2 distinct values
            best = max(best, j - i)              # 🎯 maximum valid window length from [i..j)
        return best

print(Solution().lengthOfLongestSubstringTwoDistinct('abace'))