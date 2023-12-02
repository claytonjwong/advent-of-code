#
# 1541. Minimum Insertions to Balance a Parentheses String
#
# Q: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
# A: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/discuss/793179/Javascript-Python3-C%2B%2B-double-'))'-or-single-')'
#

# concise
class Solution:
    def minInsertions(self, s: str, x = 0, cost = 0) -> int:
        N = len(s)
        i = 0
        doubleEnd = lambda i: s[i] == ')' and i + 1 < N and s[i + 1] == ')'
        while i < N:
            if s[i] == '(':                          # case '('  -> push to stack 🥞 (increment x count)
                x += 1
            else:
                if doubleEnd(i):                     # 🍔 🍔 '))' ->  0 penalty if ✅  preceeding '(' on the stack 🥞 (0 < x count)
                    cost += not x                    #               +1 penalty if 🚫  preceeding '(' on the stack 🥞 (0 < x count)
                else:                                # 🍔    ')'  -> +1 penalty if ✅  preceeding '(' on the stack 🥞 (0 < x count)
                    cost += 1 if x else 2            #               +2 penalty if 🚫  preceeding '(' on the stack 🥞 (0 < x count)
                x = x - 1 if x else 0                # always pop the corresponding '(' from stack 🥞 (decrement x count) if it exists
            i += 2 if doubleEnd(i) else 1            # skip past the 🍔 🍔 double '))' or 🍔 single ')'
        return cost + (2 * x)               # +2 penalty for each stack.length '(' remaining on the stack since each needs a 🍔 🍔 double '))' to reduce

# verbose
class Solution:
    def minInsertions(self, s: str, cost = 0) -> int:
        stack = []
        N = len(s)
        i = 0
        doubleEnd = lambda i: s[i] == ')' and i + 1 < N and s[i + 1] == ')'
        while i < N:
            if s[i] == '(':                          # case '('  -> push to stack 🥞 (increment x count)
                stack.append('(')
            else:
                if doubleEnd(i):                     # 🍔 🍔 '))' ->  0 penalty if ✅  preceeding '(' on the stack 🥞 (0 < x count)
                    cost += not len(stack)           #               +1 penalty if 🚫  preceeding '(' on the stack 🥞 (0 < x count)
                else:                                # 🍔    ')'  -> +1 penalty if ✅  preceeding '(' on the stack 🥞 (0 < x count)
                    cost += 1 if len(stack) else 2   #               +2 penalty if 🚫  preceeding '(' on the stack 🥞 (0 < x count)
                if len(stack):
                    stack.pop()                      # always pop the corresponding '(' from stack 🥞 (decrement x count) if it exists
            i += 2 if doubleEnd(i) else 1            # skip past the 🍔 🍔 double '))' or 🍔 single ')'
        return cost + (2 * len(stack))               # +2 penalty for each stack.length '(' remaining on the stack since each needs a 🍔 🍔 double '))' to reduce
