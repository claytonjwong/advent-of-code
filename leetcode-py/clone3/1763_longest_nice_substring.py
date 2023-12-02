#
# 1763. Longest Nice Substring
#
# Q: https://leetcode.com/problems/longest-nice-substring/
# A: https://leetcode.com/problems/longest-nice-substring/discuss/1074560/Kt-Js-Py3-Cpp-Recursive
#

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        best = ''
        def go(s):
            nonlocal best
            seen = set(s)
            isNice = lambda c: c.lower() in seen and c.upper() in seen
            for i in range(len(s)):
                if not isNice(s[i]):
                    go(s[:i]); go(s[i + 1:])
                    return
            if len(best) < len(s):
                best = s
        go(s)
        return best
