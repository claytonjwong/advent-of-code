#
# 735. Asteroid Collision
#
# Q: https://leetcode.com/problems/asteroid-collision/
# A: https://leetcode.com/problems/asteroid-collision/discuss/109683/Kt-Js-Py3-Cpp-Simulate-Collisions
#

from typing import List

class Solution:
    def asteroidCollision(self, pre: List[int]) -> List[int]:
        while True:
            ok = True
            cur = []
            for i in range(0, len(pre)):
                # ✅ case 1: no collision
                if not len(cur) or cur[-1] < 0 or (0 <= cur[-1] and 0 <= pre[i]):
                    cur.append(pre[i])
                    continue
                # 🚫 case 2: 💥 collision
                ok = False
                last = cur.pop()
                if abs(last) != abs(pre[i]):
                    cur.append(pre[i] if abs(last) < abs(pre[i]) else last)
            pre, cur = cur, pre
            if ok:
                break
        return pre
