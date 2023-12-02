#
# 227. Basic Calculator II
#
# Q: https://leetcode.com/problems/basic-calculator-ii/
# A: https://leetcode.com/problems/basic-calculator-ii/discuss/947645/Kt-Js-Py3-Cpp-Stack
#

class Solution:
    def calculate(self, expr: str, x = 0, op = '+') -> int:
        S = []
        N = len(expr)
        for i in range(N + 1):
            if i < N and expr[i] == ' ':
                continue
            if i < N and expr[i].isdigit():
                x = 10 * x + ord(expr[i]) - ord('0')
                continue
            if op == '+': S.append(x)
            if op == '-': S.append(-x)
            if op == '*': S.append(S.pop() * x)
            if op == '/': S.append(int(S.pop() / x))
            x = 0; op = expr[i] if i < N else '?'
        return sum(S)
