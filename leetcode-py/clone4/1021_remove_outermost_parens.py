#
# 1021. Remove Outermost Parentheses
#
# Q: https://leetcode.com/problems/remove-outermost-parentheses/
# A: https://leetcode.com/problems/remove-outermost-parentheses/discuss/275804/Javascript-Python3-C%2B%2B-Stack-solutions
#

class Solution:
    def removeOuterParentheses(self, parens: str) -> str:
        s, x = [], []
        for c in parens:
            if c == ')': s.pop()
            if len(s):   x.append(c)
            if c == '(': s.append(c)
        return ''.join(x)
