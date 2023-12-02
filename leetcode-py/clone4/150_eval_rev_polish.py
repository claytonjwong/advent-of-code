#
# 150. Evaluate Reverse Polish Notation
#
# Q: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# A: https://leetcode.com/problems/evaluate-reverse-polish-notation/discuss/893409/Kt-Js-Py3-Cpp-Stack-(c-a-op-b)
#

from typing import List

class Solution:
    def evalRPN(self, words: List[str]) -> int:
        is_number = lambda x: x.isnumeric() or (x[0] == '-' and 1 < len(x))
        S = []
        for x in words:
            if is_number(x):
                S.append(int(x))
            else:
                b = S.pop()
                a = S.pop()
                c = a + b if x == '+' else a - b if x == '-' else a * b if x == '*' else a // b if (0 <= a and 0 <= b or (a < 0 and b < 0)) else ceil(a / b)
                S.append(c)
        return S.pop()
