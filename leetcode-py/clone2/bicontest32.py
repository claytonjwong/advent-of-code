#
# https://leetcode.com/contest/biweekly-contest-32/
# https://www.youtube.com/watch?v=xuyvk8ycHFs
#
# Rank            Name            Score    Finish Time     Q1 (3)       Q2 (4)    Q3 (5)    Q4 (6)
# 6181 / 10463    claytonjwong    3        0:46:48         0:36:48 *2
#

from typing import List

#
# 1539. Kth Missing Positive Number
#
# Q: https://leetcode.com/problems/kth-missing-positive-number/
# A: https://leetcode.com/problems/kth-missing-positive-number/discuss/780016/Javascript-Python3-C%2B%2B-Seen-values
#
class Solution:
    def findKthPositive(self, A: List[int], K: int) -> int:
        seen = set(A)
        i = 1
        while True:
            if not i in seen:
                K -= 1
                if K == 0:
                    return i
            i += 1

#
# 1540. Can Convert String in K Moves
#
# Q: https://leetcode.com/problems/can-convert-string-in-k-moves/
# A: https://leetcode.com/problems/can-convert-string-in-k-moves/discuss/780454/Javascript-Python3-C%2B%2B-add-%2B-del-needs
#
class Solution:
    def canConvertString(self, s: str, t: str, K: int) -> bool:
        if len(s) != len(t):
            return False
        need, needs = {}, 0
        # ✅ add needs
        for i in range(len(s)):
            diff = (ord(t[i]) - ord(s[i]) + 26) % 26
            if diff:
                if not diff in need:
                    need[diff] = 0
                need[diff] += 1
                needs += 1
        # 🚫 del needs
        for i in range(1, K + 1):
            if not needs:
                break
            diff = i % 26
            if diff in need and need[diff]:
                need[diff] -= 1
                needs -= 1
        return not needs # 🎯 no needs
