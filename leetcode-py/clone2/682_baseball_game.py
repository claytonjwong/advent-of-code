#
# 682. Baseball Game
#
# Q: https://leetcode.com/problems/baseball-game/
# A: https://leetcode.com/problems/baseball-game/discuss/107929/C%2B%2B-and-Javascript-solutions
#

from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s = []
        for op in ops:
            if op == "+":
                s.append(s[-2] + s[-1])
            elif op == "D":
                s.append(2 * s[-1])
            elif op == "C":
                s.pop()
            else:
                s.append(int(op))
        return sum(s)
