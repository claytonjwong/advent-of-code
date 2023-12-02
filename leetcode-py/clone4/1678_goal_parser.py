#
# 1678. Goal Parser Interpretation
#
# Q: https://leetcode.com/problems/goal-parser-interpretation/
# A: https://leetcode.com/problems/goal-parser-interpretation/discuss/962100/Kt-Js-Py3-Cpp-Linear-Scan-%2B-Last-Seen
#

class Solution:
    def interpret(self, s: str, last = 'x') -> str:
        ans = []
        for c in s:
            if c == 'G': ans.append('G')
            if c == ')': ans.append('o' if last == '(' else 'al')
            last = c
        return ''.join(ans)
