#
# 1540. Can Convert String in K Moves
#
# Q: https://leetcode.com/problems/can-convert-string-in-k-moves/
# A: https://leetcode.com/problems/can-convert-string-in-k-moves/discuss/780454/Javascript-Python3-C%2B%2B-add-%2B-del-needs
#

# verbose
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

# concise
class Solution:
    def canConvertString(self, s: str, t: str, T: int) -> bool:
        if len(s) != len(t):
            return False
        need = {}
        # ✅ add needs
        for i in range(len(s)):
            k = (ord(t[i]) - ord(s[i])) % 26
            if k:
                if not k in need:
                    need[k] = 0
                need[k] += 1
        # check if T is 🚫 insufficient for the needs
        for k, cnt in need.items():
            if T < k + (cnt - 1) * 26:
                return False
        return True # 🎯 T is sufficient for the needs
