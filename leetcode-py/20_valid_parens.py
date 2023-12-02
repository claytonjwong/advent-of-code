#
# 20. Valid Parentheses
#
# Q: https://leetcode.com/problems/valid-parentheses/
# A: https://leetcode.com/problems/valid-parentheses/discuss/9214/Kt-Js-Py3-Cpp-Stack
#

class Solution:
    def isValid(self, A: str) -> bool:
        s = []
        for c in A:
            if   c == '(': s.append(')')
            elif c == '[': s.append(']')
            elif c == '{': s.append('}')
            elif not len(s) or c != s.pop():
                return False
        return not len(s)
