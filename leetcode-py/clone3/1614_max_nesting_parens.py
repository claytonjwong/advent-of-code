#
# 1614. Maximum Nesting Depth of the Parentheses
#
# Q: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# A: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/discuss/888880/Kt-Js-Py3-C%2B%2B-Count-Depth
#

class Solution:
    def maxDepth(self, s: str, cnt = 0, best = 0) -> int:
        for c in s:
            if c == '(': cnt += 1; best = max(best, cnt)
            if c == ')': cnt -= 1
        return best
